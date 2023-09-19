# Python-Redis

## Preparing
If you want to, the database using MySQL was configured to be automatically installed along with fake data using Docker-Compose.
`sudo docker-compose up -d` 

Docker-compose file is structured to run the following containers:
> MySQL 

Docker-compose version: 1.29.2


Also make sure that you have mysql connector library on your computer
It can be installed using:

` pip3 install mysql-connector-python` 

## Getting IP from the MySQL container created 
`sudo docker inspect first-mysql | grep IPAddress`

## Connecting with DB
After getting the IP from the container created by docker, update the file controllers/ConnectorBD.py with this ip.  Example: host="172.21.0.2"


After this you can run `main.py` to execute the program.

## EXTRA
### Debugging: Acessing directly MYSQL Container.
You can also access directly mysql container for debugging/testing purposes.
`sudo docker exec -it first-mysql bash` (Example for acessing docker container)
`sudo mysql -uroot -ptest123`   (Example to acess mysql inside the container with user: root & password: test123)

### Removing All Created Resources
If you want to want to remove the things created by docker-compose such as volume,image and container, you can run the following script:

`bash remove-script.sh` 
Make sure the "run-script.sh" file has the required permissions, you can use `chmod +x ./remove-script.sh` before run the code above to ensure it.


## Source
Source of Board Games Example Info: boardgamegeek.com