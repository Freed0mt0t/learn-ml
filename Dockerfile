# 🐳 ML 学习环境 —— PyTorch + Jupyter Lab
#
# 启动:
#   docker compose up -d
#
# 访问:
#   Jupyter Lab: http://localhost:8888 (token 见启动日志)
#
# GPU 版本（有 NVIDIA 显卡）:
#   docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d

FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

LABEL description="从0到1学模型训练 - 全栈 ML 环境"
LABEL maintainer="user566289"

# 避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# 系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl wget vim htop tree \
    ffmpeg libsm6 libxext6 libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Python 核心库
RUN pip install --no-cache-dir \
    jupyterlab ipywidgets ipdb \
    numpy pandas scipy \
    matplotlib seaborn plotly \
    scikit-learn xgboost lightgbm \
    tqdm rich

# 深度学习 & NLP
RUN pip install --no-cache-dir \
    transformers datasets tokenizers accelerate peft \
    sentencepiece safetensors \
    einops timm

# 实验管理 & 部署
RUN pip install --no-cache-dir \
    tensorboard wandb \
    fastapi uvicorn \
    onnx onnxruntime

# Jupyter 配置
RUN mkdir -p /root/.jupyter && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.allow_root = True" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.open_browser = False" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.token = ''" >> /root/.jupyter/jupyter_server_config.py && \
    echo "c.ServerApp.password = ''" >> /root/.jupyter/jupyter_server_config.py

WORKDIR /workspace

# 启动 Jupyter Lab
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=''", "--ServerApp.password=''"]
