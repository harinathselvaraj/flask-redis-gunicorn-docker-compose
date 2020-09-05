# Redis Flask App deployed in Docker using Docker Compose

A Python Flask application that uses Redis (seperate docker container) and gunicorn. The application uses Docker compose that builds two containers - Flask app & Redis.

# Commands
<code>
docker-compose --version
sudo docker-compose up
sudo docker-compose up --build       //use this command if the container doesn't refresh..
</code>