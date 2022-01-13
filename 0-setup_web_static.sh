#/usr/bin/env bash
# A script that sets up web server for deployment
FILE=/etc/nginx/sites_available/defult
STRING="location  /hbnb_static/ {\n alias /data/web_static/current/; \n }\n"

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p  /data/web_static/shared/
echo "software Engineering is fun" > /data/web_static/releases/test/index.html
sudo ln -sf data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "39i $STRING" $FILE
sudo service nginix restart
