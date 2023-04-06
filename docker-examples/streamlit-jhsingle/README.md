
### --  Running a streamlit example using jhsingle -- 


# To build and run this image

```
docker build -t stream-jhs .
docker run -p 8505:8505 stream-jhs
```

jhsingle by default sets the destination port to 8500, so we can map this port to the external world

# How to check jupyterhub logs

to check the Jupyterhub logs, you can go directly to check this in the docker terminal

```
jupyterhub logs
```

# Error 1

This error is a warning regarding activity reporting but is not necessary for the running of the server

```
The following env vars are required to report activity back to the hub for keep alive: JUPYTERHUB_ACTIVITY_URL (), JUPYTERHUB_SERVER_NAME()
```

# Error 2

```
Writing cookie_secret to /home/jovyan/jupyterhub_cookie_secret
...
OSError: [Errno 28] No space left on device: '/tmp/tmp_uximrrh'
```

prune the old containers

run this on your local terminal

```
docker system prune -af
```

# Error 3

```
Failed to find proxy ['configurable-http-proxy']
```

add this package to the requirements.txt

# Note

[I 2023-03-27 17:19:49.824 JupyterHub app:3197] JupyterHub is now running at http://:8000

the port is still not mapped

Adding the destination port to the command string

CMD ["jhsingle-native-proxy", "--port", "8501", "--destport", "8505", "streamlit", "run", "./app.py"]