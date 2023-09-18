FROM mysql

#MySQL docker container executes script files from /docker-entrypoint-initdb.d/ folder in the ascending order of file names
COPY CreateTables.sql /docker-entrypoint-initdb.d/
COPY InsertFakeData.sql /docker-entrypoint-initdb.d/

EXPOSE 3306