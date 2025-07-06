# Telegram Bot Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install aiogram

# Copy source code
COPY ./main.py .

# Command to run the bot
CMD ["python", "main.py"]
