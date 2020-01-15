The project has two folders.
the web folder the app.py the actual code to run the app,
requirements.txt- the requiremtns to run the code
the Dockerfile that explains how to run the web module

At the top level the file docker-compose.yml is responsible to start the aplication and control the comunications between the service modules

To run the application:

sudo docker-compose build
sudo docker-compose up
