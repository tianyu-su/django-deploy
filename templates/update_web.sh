#!/bin/bash 
echo "==== BACK SOURCE ===="
sudo tar -zcvf  /home/backup/src/<web-name>/"$(date +%Y-%m-%d-%H-%M-%S)".tar.gz --exclude=/home/<web-name>/.git --exclude=/home/<web-name>/.idea /home/<web-name>/

echo "==== FORCE PULL SOURCE ===="
cd /home/<web-name>/<web-name>
sudo git fetch --all
sudo git reset --hard origin/master
sudo git pull

sudo find -name settings.py | sudo xargs perl -pi -e 's|DEBUG = True|DEBUG = False|g'
# update seetting.py 's STATIC_URL = '/<web-name>/static/' same with nginx.conf
sudo find -name settings.py | sudo xargs perl -pi -e "s|STATIC_URL = '/static/'|STATIC_URL = '/<web-name>/static/'|g"

echo "=== RELOAD SERVICES ==="
sudo service nginx reload
sudo service supervisor restart

sudo service nginx status
sudo service supervisor status

echo "=== OPEN TEST PAGE ==="
wget --spider -nv "$(curl -s <get-server-ip>)"":<nginx-port><test-page>"
