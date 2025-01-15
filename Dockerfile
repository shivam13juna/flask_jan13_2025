# name has to be Dockerfile

FROM python:3.8-slim-buster 

# this is the base image, which contains python 3.8 and a basic skeleton linux os

WORKDIR /flask-loan-app
# name of the directory where the app will be stored

COPY artefacts/requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /flask-loan-app/
# copy everything from the current directory to the directory in the container


# python -m flask --app hello.py run --host=0.0.0.0 --port=8000

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]



#docker build -t ano .
#docker image ls
#docker run -p 8000:8000 ano

# first 8000 is the port on the host machine (my local) and the second 8000 is the port on the container

#docker container ls --all

# this will tell us the container id, which we can use to stop the container

# RUN executes the command while building the image, CMD executes the command when the container is started