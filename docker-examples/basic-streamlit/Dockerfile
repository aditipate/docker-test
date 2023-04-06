# A streamlit example for JupyterHub
FROM python:3.7

# Install Requirements
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Set app directory
WORKDIR /app
COPY . .

EXPOSE 8888

CMD ["streamlit", "run", "/app/app.py"]