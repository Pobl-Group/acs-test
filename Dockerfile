FROM mcr.microsoft.com/devcontainers/python:3.11

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
