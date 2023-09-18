#!/bin/bash

function deleting_containers() {
    sudo docker rm -f first-mysql; 
}

function deleting_image() {
    sudo docker rmi -f python-redis_db
}

function deleting_volumes(){
    sudo docker volume rm -f python-redis_myvolume
}

deleting_containers
deleting_image
deleting_volumes