# API DOCUMENTATION

This API uses Celery as a task manager to handle heavy workloads, and redis as the tasks broker.

## 1. Setup

### Redis
Redis is a messages broker used by celery to handle the tasks. To set it up on a debian based distribution follow this follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04) steps.

This tutorial helps you do the following: 

1. Install redis
2. Bind redis to localhost
3. Configure redis password
4. Disable commands to avoid malicious usage

If you are too lazy to configure the file, there is a sample file `redis.conf.example` already configured (for debian based distros), you just need to change the passwword and copy it's contents to `/etc/redis/redis.conf`

If you are using a different distribution please follow different steps to make sure redis is set up correctly. Just make sure you set up a password to avoid security issues, and it's binded to localhost.


### Celery

Start Celery 
`celery -A celery_conf worker --loglevel=info`

Enable task events to monitor status
`celery -A celery_conf control enable_events`

Monitor tasks status
`celery -A celery_conf events`
  

## 2. Endpoints
Once the server is up and running, you can check the endpoints at `https://<api_url>/docs`


# Enable traffic on port `80`
To connect to the machine, you have to allow traffic on port 80 (default https port)

### 1. Enable the firewall
`sudo ufw enable`

### 2. Allow traffic on port `80`
`sudo ufw allow {port}/tcp`

### 3. 
Check if the port is listening and allowing connections from any ip

`sudo ufw status`


# Setup Nginx 

### 1. Install nginx
sudo apt install nginx

### 2. Disable the default configuration
sudo rm /etc/nginx/sites-enabled/default

### 3.Setup a reverse proxy to redirect traffic
We will redirect all the incomming traffic from port `80` to port `8000` (fast apis's default port).

**3.1** Copy the reverse-proxy config file

`cp ~/fastapi_demo/api/config_files/reverse-proxy-yolo.conf /etc/nginx/sites-available/reverse-proxy-yolo.conf`

**3.2** Disable nginx's default config

`sudo rm /etc/nginx/sites-enabled/default`


**3.3** Enable reverse-proxy config

`sudo ln -s /etc/nginx/sites-available/reverse-proxy-yolo.conf /etc/nginx/sites-enabled/reverse-proxy-yolo.conf`

**3.4** Restart nginx to use the new configurations

`sudo systemctl restart nginx`


# Setup gunicorn
pip install gunicorn

