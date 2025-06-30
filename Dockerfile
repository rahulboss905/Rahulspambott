FROM python:3.11-slim

RUN apt update && apt install -y     build-essential     libssl-dev     libffi-dev     python3-dev     git     curl

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
