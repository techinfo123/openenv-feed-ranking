FROM python:3.10

WORKDIR /app
COPY . .

# Install only minimal dependencies (safe build)
RUN pip install --no-cache-dir numpy

CMD ["python", "main.py"]