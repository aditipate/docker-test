# A streamlit example for JupyterHub
FROM python:3.7

# Install Requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# create a user, since we don't want to run as root
RUN useradd -m jovyan
ENV HOME=/home/jovyan
WORKDIR $HOME
USER jovyan

# Set app directory
# WORKDIR /app
COPY . .

EXPOSE 8888

# CMD ["jhsingle-native-proxy", "--port", "8501", "--destport", "8505", "streamlit", "run", "./app.py", "{--}server.port", "{port}", "{--}server.headless", "True", "{--}server.enableCORS", "False"]
# CMD ["streamlit", "run", "./app.py"]
CMD ["jhsingle-native-proxy", "--port", "8501", "--destport", "8505", "streamlit", "run", "./app.py"]