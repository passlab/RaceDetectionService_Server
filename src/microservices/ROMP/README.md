# Usage

A simple web interface for quick demo is available at https://romp.racedetection.org.

The API call can be used as follows. It will return a JSON response.

```bash
curl -F 'file=@DRB003-antidep2-orig-yes.c' https://romp.racedetection.org/requests
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

### Get the docker image of ROMP

```bash
docker pull racedetection/rds:romp-tool
```
#### 1. Create a container

```bash
docker run -it --name rds_romp racedetection/rds:romp-tool bash
```

#### 2. Start a container

```bash
docker start rds_romp
```

#### 3. Enter a container

```bash
docker exec -it rds_romp bash
```

#### 4. ROMP usage

Follow the official guide or other instructions.

https://github.com/zygyz/romp


## ROMP microservice development

Flask framework under python3 has been installed in the docker image of ROMP server.
Since ROMP server is running in rootless dind mode, we have to run the official rootless dind image as docker daemon provider.

```bash
docker run --privileged --name dind-server -d -e DOCKER_TLS_CERTDIR="" docker:stable-dind-rootless --experimental
```

To deploy the ROMP server, we also need to map the host port to the docker container port.
For example, assume we have an available Flask server running on the port 5000 in the container. The port 5020 on the host is assigned to the microservice. While creating the container, the port mapping is needed as follows.

```bash
docker pull racedetection/rds:romp-server
docker run --rm -it -p 5020:5000 -d --link dind-server:docker racedetection/rds:romp-server /flask/start.sh
```

Finally, on the host browser we can access the microservice at `127.0.0.1:5020`. For other external machine, it can be accessed at `<host_ip>:5020`.


