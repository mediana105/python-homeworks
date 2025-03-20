FROM python:3.9-slim AS builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["sh", "-c", "python latex_generator/main.py && pdflatex -output-directory artifacts/task_3 artifacts/task_2/main.tex"]

# Launching a docker container:
# 1. docker build -t latex_generator .
# 2. docker run --rm -v $(pwd):/app latex_generator