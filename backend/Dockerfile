# Backend Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn pymongo requests gologin playwright

# Install Playwright browsers
RUN playwright install --with-deps

# Copy source code
COPY . .

# Expose port and run the application
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
