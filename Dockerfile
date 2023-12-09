FROM python:3.11.2-buster

WORKDIR /usr/src/app

# ディレクトリ全体をコピー
COPY . /usr/src/app

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

