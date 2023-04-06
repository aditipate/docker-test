FROM python:3.7
# Install Requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# create a user, since we don't want to run as root
RUN useradd -m jovyan
ENV HOME=/home/jovyan
WORKDIR $HOME
USER jovyan

EXPOSE 8888

WORKDIR /app

COPY app.py /app/app.py

CMD ["jhsingle-native-proxy", "--destport", "8505", "streamlit", "run", "app.py", "{--}server.port", "{port}", "{--}server.headless", "True", "{--}server.enableCORS", "False"]
