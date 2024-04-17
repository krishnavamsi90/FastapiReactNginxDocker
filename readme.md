# FastAPI React Nginx Docker Minimalistic Example
A fixed and slighlty simplified version of https://github.com/vikramgulia/fastapi-react/tree/master 

# About
The project has an nginx proxy, a react frontend, and a fastapi backend.

When you build the docker compose, html and javascript are produced from the frontend files, the fastapi backend is activated, and an nginx proxy is activated, which serves the html and javascript in most paths, and routes /api to fastapi.

# Usage
You can run it with docker compose up --build . You can then visit the webpage at http://localhost


# Important warning
This project is very simple, and could be a good introduction to these tools BUT:
- It uses outdated dependancies, such as create react app
- Doesn't use all best practices. For example, it doesnt have a separate compose for development, and doesn't allow hot reloading of files during development. Therefore, developing with the docker container would be extremely impractical.

Alternatively, I suggest you use: [FastAPI React MongoDB Docker](https://github.com/jonasrenault/fastapi-react-mongodb-docker/) or possibly [Full Stack FastApi PosgreSQL](https://github.com/whythawk/full-stack-fastapi-postgresql). There are other options, incluiding  [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template), but many of them are currently broken, including that one, at least according to the issues.
