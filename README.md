# SCS centrality metrics

# Instructions to build and run Docker container

* Go to the project directory (where `Dockerfile` is)
* Build Flask image:

```bash
docker build -t myimage .
```

* Run a container based on the image:

```bash
docker run -d --name mycontainer -p 80:5000 myimage
```

Application should be available in Docker container's URL, for example: <a href="http://192.168.99.100" target="_blank">http://192.168.99.100</a> or <a href="http://127.0.0.1" target="_blank">http://127.0.0.1</a>
