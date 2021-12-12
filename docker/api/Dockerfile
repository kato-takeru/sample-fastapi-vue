FROM python:3.7

WORKDIR /var/www/fastapi

ADD requirements.txt .

# コンテナ内で必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \                                                      
    build-essential \   
    gcc \
    libxslt-dev
# requirements.txtにリストされたパッケージをインストールする
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]