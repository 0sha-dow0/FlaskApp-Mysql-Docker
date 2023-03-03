# FlaskApp-Mysql-Docker

# Mysql Docker (Step-1)
- Dockerize MySQL in a container
- Run command ***docker run --name "container_name" -p 3306:3306 -e MYSQL_ROOT_PASSWORD="your_psswd" -d mysql*** where container_name is going to be your container name and your_psswd is the password to connect to the MySQL instance
- use MySQL workbench to connect  and test the instance by giving the correct hostname and username as ***root***
- When using DBeaver  Goto Driver Properties and change allowPublicKeyRetrieval drop down to TRUE
- Once the connection is successful create db and table and insert values or run schema.sql

# Flask App Docker (Step-2)
- Have Docker Installed ***GLOBALLY*** in your system
- Clone the repo in a folder
- Run the command  ***docker build -t "your_tag" .***
- Where docker will build the image and put it in a destination file which is represented here with a dot(***.***)
- Now run  ***docker run -d -p 5000:5000 "your_tag"*** 
- -d in detached mode so that the terminal becomes free
- -p to map your container port with the server port 


