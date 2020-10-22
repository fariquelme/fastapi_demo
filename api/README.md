# API DOCUMENTATION

## 2. Endpoints
Once the server is up and running, you can check the endpoints at `https://<api_url>/docs`


# Enable traffic on port `80`
To connect to the machine, you have to allow traffic on port 80 (default https port)

### 1. Enable the firewall
`sudo ufw enable`

### 2. Allow traffic on port `80` and ssh
`sudo ufw allow {port}/tcp`
`sudo ufw allow ssh`


### 3. Check if the port is listening and allowing connections from any ip

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


### Gunicorn

Before following the next steps edit the service definition `api/config_files/gunicorn_api.service` and replace all the <usernmae> with the corresponding username

1. Copy the service definition to let the system manager use it

`sudo cp api/config_files/gunicorn_api.service /etc/systemd/system/`

2. Enable the service to run on startup

`sudo systemctl enable gunicorn_api.service`

3. Enable start the service

`sudo systemctl start gunicorn_api.service`


4. Check the service status to see if it is active

`sudo systemctl status gunicorn_api.service`
