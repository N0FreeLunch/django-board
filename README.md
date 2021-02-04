# django-board


## server setting
### run python vertual environment
```
    pip install gunicorn
```

### go to django root directory
```
    gunicorn --bind 0:8000 config.wsgi:application
```

### setting for nginx socket connection
```
    gunicorn --bind unix:/tmp/gunicorn.sock config.wsgi:application
```

### Gunicorn Setting
in server
```
    sudo vi /etc/systemd/system/mysite.service
```
(press i key)
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/projects/django-board
# EnvironmentFile=/home/ubuntu/venvs/mysite.env
ExecStart=/home/ubuntu/venvs/mysite/bin/gunicorn \
        --workers 2 \
        --bind unix:/tmp/gunicorn.sock \
        config.wsgi:application
[Install]
WantedBy=multi-user.target
```
(esc) :qw!

#### setting socket connection
```
    --bind unix:/tmp/gunicorn.sock \ 
```

### run gunicorn
```
    cd /etc/systemd/system
    sudo systemctl start mysite.service
    sudo systemctl status mysite.service
```

### run gunicorn when server restart (use enable)
```
    sudo systemctl enable mysite.service
```

### stop running gunicorn
```
    sudo systemctl stop mysite.service
```

### restart gunicorn
```
    sudo systemctl restart mysite.service
```


## install nginx
```
    sudo apt install nginx
    cd /etc/nginx/sites-available/
    sudo vi mysite
```


```
server {
        listen 80;
        server_name your.server.domain;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /home/ubuntu/projects/django-board/static;
        }

        location / {
                include proxy_params;
                proxy_pass http://unix:/tmp/gunicorn.sock;
        }
}
```


```
    cd /etc/nginx/sites-enabled/
    ls
    sudo rm default
    sudo ln -s /etc/nginx/sites-available/mysite
    ls
```