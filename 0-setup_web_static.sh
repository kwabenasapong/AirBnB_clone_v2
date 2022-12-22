#!/usr/bin/env bash
# configuring my servers as web servers

# Update and install nginx
sudo apt update -y
sudo apt install nginx -y

# Create necessary directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create index.html
echo "it works" | sudo tee /data/web_static/releases/test/index.html

# Change ownership
sudo chown -hR ubuntu:ubuntu /data/

# Create symlinks
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo rm -rf /etc/nginx/sites-enabled
sudo ln -sf /etc/nginx/sites-available/ /etc/nginx/sites-enabled

# configure Nginx Servers
replace="server_name _;"
new="server_name _;\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"
sudo sed -i "s/$replace/$new/" /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
