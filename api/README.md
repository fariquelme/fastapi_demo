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
