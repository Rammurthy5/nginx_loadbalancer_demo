apt upgrade -y
apt install python3.8 python3.8-dev python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev python3-pip python3.8-venv apt libpython3.7-dev

Edit /etc/nginx/sites-enabled/default and comment IPv6 out:

listen [::]:80 default_server;

pip install uwsgi

install nginx 

setup ssl certificates in /etc/nginx/nginx.conf
Make thi config change, 
search for ssl on;
 
add these below that, 
		ssl_certificate path to pem;
        ssl_certificate_key path to key;


cp /etc/nginx/uwsgi_params .

place python_services.ini (project root dir) under /python_services dir.

change logto values in python_services.ini

rm /etc/nginx/sites-enabled/default

create /etc/nginx/sites-available/python_services
sudo ln -s /etc/nginx/sites-available/python_services /etc/nginx/sites-enabled/.

nginx -t 

restart nginx

Run uwsgi <.ini> file in nohup. 

check https://ip:8003/test 