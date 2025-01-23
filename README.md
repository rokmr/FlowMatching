[![Notes](https://img.shields.io/badge/Keynote-blue?style=flat&logo=slides&logoColor=white&logoSize=amg&color=%23ADADFF)](https://www.icloud.com/keynote/0e5fXZn-TsuniKe6LMa7j-gxw#FlowMatching) [![Open in GitHub Codespaces](https://img.shields.io/badge/Open_in_GitHub_Codespaces-blue?style=flat&logo=github&logoColor=white&logoSize=amg&color=%23222222)](https://codespaces.new/rokmr/FlowMatching?quickstart=1)

[Shared Drive](https://drive.google.com/drive/folders/1ofUpdHjyODpgiXojPMI8qsnqOLADDe-J?usp=sharing)

# FlowMatching

# Github codespace

```bash
conda init bash && source ~/.bashrc && conda activate flow_matching
```

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
Flow Matching Guide and Code || [paper](https://arxiv.org/pdf/2412.06264) || [code](https://github.com/facebookresearch/flow_matching) || [page](https://facebookresearch.github.io/flow_matching/)
