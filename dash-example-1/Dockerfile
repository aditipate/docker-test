FROM python:3.9-slim
COPY . /app 
WORKDIR /app    

RUN pip3 install -r requirements.txt

# CMD python3 app.py

#CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8050", "app:server"] 

