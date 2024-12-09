FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ./scripts ./scripts
COPY ./datasets ./datasets
COPY ./models ./models
COPY ./reports ./reports

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define entry point
CMD ["python", "./scripts/evaluate_model.py"]
