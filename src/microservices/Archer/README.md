# Usage

A simple web interface for quick demo is available at https://archer.racedetection.org.

The API call can be used as follows. It will return a JSON response.

```bash
curl -F 'file=@DRB003-antidep2-orig-yes.c' https://archer.racedetection.org/requests
```

# Deployment

## Prerequisite

1. OS:
Ubuntu 18.04

1. Install docker
```bash
sudo apt update
sudo apt install docker.io
```

### Get the docker image of Archer

```bash
docker pull racedetection/rds:archer-tool
```
#### 1. Create a container

```bash
docker run -it --name rds_archer racedetection/rds:archer-tool bash
```

#### 2. Start a container

```bash
docker start rds_archer
```

#### 3. Enter a container

```bash
docker exec -it rds_archer bash
```

#### 4. Archer usage

Follow the official guide or other instructions.

https://github.com/PRUNERS/archer


## Archer microservice development

Flask framework under python3 has been installed in the docker image of Archer server.
Since Archer server is running in rootless dind mode, we have to run the official rootless dind image as docker daemon provider.

```bash
docker run --privileged --name dind-server -d -e DOCKER_TLS_CERTDIR="" docker:stable-dind-rootless --experimental
```

To deploy the Archer server, we also need to map the host port to the docker container port.
For example, assume we have an available Flask server running on the port 5000 in the container. The port 5010 on the host is assigned to the microservice. While creating the container, the port mapping is needed as follows.

```bash
docker pull racedetection/rds:archer-server
docker run --rm -it -p 5010:5000 -d --link dind-server:docker racedetection/rds:archer-server /flask/start.sh
```

Finally, on the host browser we can access the microservice at `127.0.0.1:5010`. For other external machine, it can be accessed at `<host_ip>:5010`.


