# 使用官方 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY src/ ./src/

# 暴露端口 (如果需要)
# EXPOSE 8000

# 设置默认命令
CMD ["python", "./src/greet.py"]
