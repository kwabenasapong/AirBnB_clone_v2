#!/usr/bin/env bash
# configuring my servers as web servers
sudo apt update -y
sudo apt install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "it works" | sudo tee /data/web_static/releases/test/index.html
sudo chown -hR ubuntu /data/
sudo chgrp -hR ubuntu /data/
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo rm -rf /etc/nginx/sites-enabled
sudo ln -sf /etc/nginx/sites-available/ /etc/nginx/sites-enabled
replace="server_name _;"
new="server_name kwabenasapong.tech;\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"
sudo sed -i "s/$replace/$new/" /etc/nginx/sites-enabled/default
sudo service nginx restart
