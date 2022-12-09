#!/usr/bin/env bash
#Creation of files and others for web static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir data/web_static/releases/test/
sudo mkdir data/web_static/shared/
sudo echo "<html>
         <head>
         </head>
         <body>
             Holberton School
         </body>
      </html>" > /data/web_static/releases/test/index.html
sudo ln -nsf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '72i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enable/default 
sudo service nginx restart
