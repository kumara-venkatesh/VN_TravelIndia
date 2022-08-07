# base image 
FROM python:3.10

# setup environment variable  
ENV DockerHOME=/home/app/webapp

# set work directory  
RUN mkdir -p $DockerHOME

# where your code lives  
WORKDIR $DockerHOME

# set environment variables 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy whole project to your docker home directory. 
#COPY . $DockerHOME

#Copy only requirements.txt whole project will mount
COPY requirements.txt $DockerHOME/requirements.txt

# Upgrade pip version if there's any latest version available 
RUN pip install --upgrade pip

# run this command to install all dependencies  
RUN pip install -r requirements.txt

# port where the Django app runs  
EXPOSE 8000

# start server  
CMD python manage.py runserver 0.0.0.0:8000
