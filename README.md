# Python-Redis

## Installing
If you want to, the database using MySQL was configured to be automatically installed along with fake data using Docker-Compose.
`sudo docker-compose up -d` 

Docker-compose file is structured to run the following containers:
> MySQL 

Docker-compose version: 1.29.2


Also make sure that you have mysql connector library on your computer
It can be installed using:

` pip3 install mysql-connector-python` 


## Debugging 
### Getting IP from the MySQL container created 
`sudo docker inspect first-mysql | grep IPAddress`

### Acessing directly the Container.
`docker exec -it first-mysql bash` (Example for acessing mysql container)
`mysql -uroot -ptest123`   (Example for accessing mysql with user: root & password: test123)


## Removing
If you want to want to remove the things created by docker-compose such as volume,image and container, you can run the following script:

`bash remove-script.sh` 
Make sure the "run-script.sh" file has the required permissions, you can use `chmod +x ./remove-script.sh` before run the code above to ensure it.