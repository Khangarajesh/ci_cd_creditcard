#seeting thr base image of python with some preinstalled limited libraries (slim means  python with limited installed lib)
FROM python:3.8-slim 

#set the working directory which will consist all the required files to contenarize inorder to run the app 
WORKDIR /app_docker

#copy the necessary files in the folder 
COPY app.py /app_docker/app.py
COPY model.joblib /app_docker/model.joblib
COPY requirements.txt /app_docker/requirements.txt

#install the libraries present in requirements.txt
RUN pip install -r requirements.txt

#run the app.py using python
CMD ["python", "app.py"]