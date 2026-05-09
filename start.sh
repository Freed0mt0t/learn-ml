#!/bin/bash
# ============================================
#  ML 学习环境快速启动脚本
# ============================================
set -e

cd "$(dirname "$0")"

echo "🐳 启动 ML 学习环境..."
echo ""

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo "❌ 未安装 Docker，请先安装: https://docs.docker.com/get-docker/"
    exit 1
fi

# 检查 GPU
HAS_GPU=false
if docker run --rm --gpus all pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime nvidia-smi &> /dev/null 2>&1; then
    HAS_GPU=true
fi

COMPOSE_FILES="-f docker-compose.yml"

if $HAS_GPU; then
    echo "🎮 检测到 GPU，启用 GPU 加速"
    COMPOSE_FILES="$COMPOSE_FILES -f docker-compose.gpu.yml"
else
    echo "💻 未检测到 GPU，使用 CPU 模式"
fi
echo ""

# 构建并启动
echo "🔨 构建镜像（首次较慢，后续秒启动）..."
docker compose $COMPOSE_FILES build

echo "🚀 启动容器..."
docker compose $COMPOSE_FILES up -d

echo ""
echo "========================================"
echo "✅ 环境就绪！"
echo ""
echo "📓 Jupyter Lab:  http://localhost:8888"
echo "📊 TensorBoard:  http://localhost:6006"
echo ""
echo "常用命令:"
echo "  查看日志:  docker compose logs -f"
echo "  进入容器:  docker compose exec ml-lab bash"
echo "  停止环境:  docker compose down"
echo "  重启环境:  docker compose restart"
echo "========================================"
