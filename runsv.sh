#!/bin/bash
#Scriot to deploy ecom

configure (){
    echo "configure server"
    sudo apt update
    sudo apt install gcc
    sudo apt install apache2
    sudo apt install python, pip
    pip3 install django
    pip3 install -r requirements.txt
    pip3 install virtualenv
}

thisprojectpath="general-model-shop"
thisproject="basename $thisprojectpath"
namerepo="home/ubuntu/$thisproject"
nameenv="$namerepo-env"

configvenv (){
    virtualenv $nameenv
    source "$nameenv/bin/activate"
    pip install django
}


runserver (){
    cd $namerepo
    python ecom/manage.py collectstatic -y
    python ecom/manage.py makemigrations
    python ecom/manage.py migrate
    python ecom/manage.py runserver
}

configure && configvenv && runserver
