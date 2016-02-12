#Jax
function vdj(){
    source ~/dev/env/bin/activate
}
nihao=/home/wang/development/python

#go to jekyll blog project
function blog(){
    cd ~/dev/wfsly.github.io
}

#run the weChat test server on port 80
function run(){
    cd /home/wang/dev/weChat
    sudo /home/wang/dev/env/bin/python manage.py runserver 0.0.0.0:80
}

#run ngrok
function rng(){
    cd /home/wang/dev/tools/ngrok
    ./ngrok -config=ngrok.cfg -subdomain wx192 80
}

#go to weChat project
function we(){
    cd /home/wang/dev/weChat
}
