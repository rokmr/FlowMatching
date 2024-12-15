FROM mcr.microsoft.com/devcontainers/universal:2

WORKDIR /app

# Install dependencies from environment.yml (assuming it exists)
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -afy

# Set default shell and activate "flow_matching" environment
SHELL ["conda", "run", "-n", "flow_matching", "/bin/bash", "-c"]

# Optional: Install additional packages after Conda environment activation
RUN conda run -n "flow_matching" pip install --upgrade pip

# Optional: Customize working directory within the container
# WORKDIR /path/to/your/project