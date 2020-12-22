#!/usr/bin/env bash
# Script that sets up web servers

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web/static/releases/test
echo "testing Nginx config" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
