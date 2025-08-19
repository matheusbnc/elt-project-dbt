FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Cria diretório para profiles.yml
RUN mkdir -p /root/.dbt

# Copia profiles.yml e a chave de serviço
COPY profiles/profiles.yml /root/.dbt/profiles.yml
COPY profiles/service_account.json /root/.dbt/service_account.json

CMD [ "bash" ]
