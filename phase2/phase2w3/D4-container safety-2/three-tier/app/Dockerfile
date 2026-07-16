FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN useradd --create-home --shell /bin/bash nonroot
USER nonroot

EXPOSE 5000
CMD ["python", "app.py"]