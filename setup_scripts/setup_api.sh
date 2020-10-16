#!/bin/bash

# Exit on error
set -e

# Install model python packages
pip install -r requirements.txt

# Install api python packages
pip install -r api/requirements.txt

# Install system packages
sudo apt update && sudo apt install redis-server

# Copy default redis configuration (includes default password, should be changed)
sudo cp ./api/config_files/redis.conf.example /etc/redis/redis.conf

# Restart redis to reload configuration
sudo systemctl restart redis.service

# Check redis status
sudo systemctl status redis | grep Active

# Copy defualt env variables (includes default reddis password)
cp .env.example .env

tput setaf 2; echo 'done'; tput sgr0;
