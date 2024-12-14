[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/rokmr/FlowMatching?quickstart=1)
# FlowMatching

# Environment Setup
```bash
conda env create -f environment.yml
conda activate flow_matching
```

# Setup for original [flowmatching](https://github.com/facebookresearch/flow_matching.git)
First time setup
```bash
git subtree add --prefix=external/flow_matching https://github.com/facebookresearch/flow_matching.git main --squash
```

To pull changes from `flow_matching`
```bash
git subtree pull --prefix=external/flow_matching https://github.com/facebookresearch/flow_matching.git main --squash
```

# References
Flow Matching Guide and Code || [paper](https://arxiv.org/pdf/2412.06264) || [code](https://github.com/facebookresearch/flow_matching)