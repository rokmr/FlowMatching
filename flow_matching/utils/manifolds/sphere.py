# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the CC-by-NC license found in the
# LICENSE file in the root directory of this source tree.

import torch
from torch import Tensor

from flow_matching.utils.manifolds import Manifold


class Sphere(Manifold):
    """Represents a hyperpshere in :math:`R^D`. Isometric to the product of 1-D spheres."""

    EPS = {torch.float32: 1e-4, torch.float64: 1e-7}

    def expmap(self, x: Tensor, u: Tensor) -> Tensor:
        norm_u = u.norm(dim=-1, keepdim=True)
        exp = x * torch.cos(norm_u) + u * torch.sin(norm_u) / norm_u
        retr = self.projx(x + u)
        cond = norm_u > self.EPS[norm_u.dtype]

        return torch.where(cond, exp, retr)

    def logmap(self, x: Tensor, y: Tensor) -> Tensor:
        u = self.proju(x, y - x) # Project y-x onto tangent space at x
        dist = self.dist(x, y, keepdim=True)
        cond = dist.gt(self.EPS[x.dtype])
        result = torch.where(
            cond,
            u * dist / u.norm(dim=-1, keepdim=True).clamp_min(self.EPS[x.dtype]),
            u,
        )
        return result

    def projx(self, x: Tensor) -> Tensor:
        return x / x.norm(dim=-1, keepdim=True)

    def proju(self, x: Tensor, u: Tensor) -> Tensor:
        """Project vector u onto the tangent space at point x on the sphere.
        
        This implements the projection formula for spherical manifolds:
        proj_x(u) = u - <x,u>x

        where <x,u> is the inner product between x and u. This removes any component
        of u that points in the radial direction (parallel to x), leaving only the
        tangential components.

        Example:

        u = u cos \theta  i + u sin \theta j
        u = u_i + u_j 

        u_i : Parallel to x
        u_j : Tangential to x

        # Remove parallel component from u
        result = u - u_i 
        Find u_i

        u_i = (x * u).sum(dim=-1, keepdim=True) * x # x is unit vector along parallel direction
        
        Args:
            x (Tensor): point on the sphere (normalized to unit length)
            u (Tensor): vector to be projected onto tangent space at x

        Returns:
            Tensor: projected vector in the tangent space at x
        """
        return u - (x * u).sum(dim=-1, keepdim=True) * x

    def dist(self, x: Tensor, y: Tensor, *, keepdim=False) -> Tensor:
        inner = (x * y).sum(-1, keepdim=keepdim)
        return torch.acos(inner)
