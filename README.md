# Personal Website

Created while learning docker and such, personel website hosting on docker

## Used Technologies

Used Docker for containerizing, Fastapi for backend, next.js for frontend and nginx for reverse proxy with load balancing


## How to use

First step is to add .env file to fastapi, instructions are in fastapi/README.md

With docker compose whole project can be deployed with <code>docker compose up </code>, for detached mode add -d arg. Added <code> run.sh</code> for easy deployment with force building and certbot management.

