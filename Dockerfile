# Base com Python 3.11
FROM python:3.11-slim

# Instala pacotes essenciais
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    vim \
    nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Porta exposta (se for usar API)
EXPOSE 8080

# Comando padrão
CMD ["/bin/bash"]
