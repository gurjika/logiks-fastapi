#!/bin/bash
cd /home/ec2-user/app
echo "Fetching secrets from AWS Secrets Manager and writing to .env file..."

aws secretsmanager get-secret-value --secret-id prod/logiks \
  --query SecretString --output text | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' > /home/ec2-user/app/.env

echo ".env file created at /home/ec2-user/app/.env:"
sudo docker-compose up --build -d 