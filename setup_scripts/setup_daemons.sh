#!/bin/bash
# Exit on error
set -e

# Enable gunicorn WSGI http server 
sudo cp ../api/config_files/gunicorn_api.service /etc/systemd/system/

# Replace username placeholder with current user
sudo sed -i "s/<username>/$USER/g" /etc/systemd/system/gunicorn_api.service

# Enable daemon
sudo systemctl enable gunicorn_api.service

# Start daemon
sudo systemctl start gunicorn_api.service

# check daemon status
sudo systemctl status gunicorn_api.service | grep Active

# Install Nginx
sudo apt update && sudo apt install nginx -y

# Enable firewall
sudo ufw enable

# Enable traffic on port 80
sudo ufw allow 80/tcp
# Enable ssh connections
sudo ufw allow ssh

# Add gunicorn server reverse proxy setting
sudo cp ../api/config_files/reverse-proxy-yolo.conf /etc/nginx/sites-available/reverse-proxy-yolo.conf

# Remove default nginx config for port 80
sudo rm -f /etc/nginx/sites-enabled/default

# Enable gunicorn's reverse proxy
sudo ln -s /etc/nginx/sites-available/reverse-proxy-yolo.conf /etc/nginx/sites-enabled/reverse-proxy-yolo.conf

# Restart nginx to reload configurations
sudo systemctl restart nginx

# check nginx status
sudo systemctl status nginx | grep Active

tput setaf 2; echo 'done'; tput sgr0;
