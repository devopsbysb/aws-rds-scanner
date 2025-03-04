FROM alpine:latest

# Install Python and pip
RUN apk add --no-cache python3 py3-pip && \
    pip install --no-cache-dir --break-system-packages boto3

# Set working directory
WORKDIR /app

# Copy the script
COPY aws_rds_scanner.py /app/

# Set entrypoint
ENTRYPOINT ["python3", "/app/aws_rds_scanner.py"]

