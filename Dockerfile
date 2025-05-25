FROM python:3.11-slim

WORKDIR /app
COPY ./app /app/

CMD ["python", "main.py"]

# 既存のDockerfileにこの1行を追加してみてください
RUN echo "Docker build works!" > /echo_test.txt
# 環境変数を設定
ENV APP_ENV=development