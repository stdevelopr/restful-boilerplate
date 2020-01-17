## Restful API boilerplate

This project has two folders:
- web folder:\
(contains the files)\
*app.py* - wich is responsible to run the app\
*requirements.txt*- the requiremtns to run the code\
*Dockerfile* - explains how to run the web module

- db folder
(contains the files)\
*Dockerfile* - explains how to run the database

At the top level the file docker-compose.yml is responsible to start the aplication and control the comunications between the service modules

### To run the application:

`sudo docker-compose build`\
`sudo docker-compose up`
