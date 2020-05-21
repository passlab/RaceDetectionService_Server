# Usage

A simple web interface for quick demo is available at https://tsan.racedetection.org.

The API call can be used as follows. It will return a JSON response.

```bash
curl -F 'file=@DRB003-antidep2-orig-yes.c' https://tsan.racedetection.org/requests
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

### Get the docker image of TSan

```bash
docker pull racedetection/rds:tsan-tool
```
#### 1. Create a container

```bash
docker run -it --name rds_tsan racedetection/rds:tsan-tool bash
```

#### 2. Start a container

```bash
docker start rds_tsan
```

#### 3. Enter a container

```bash
docker exec -it rds_tsan bash
```

#### 4. ThreadSanitizer usage

Follow the official guide or other instructions.

https://clang.llvm.org/docs/ThreadSanitizer.html

https://github.com/RaceDetectionService/RaceDetectionService_Server/blob/master/tools_output/README.md


## TSan microservice development

Flask framework under python3 has been installed in the docker image of Tsan server.
Since TSan server is running in rootless dind mode, we have to run the official rootless dind image as docker daemon provider.

```bash
docker run --privileged --name dind-server -d -e DOCKER_TLS_CERTDIR="" docker:stable-dind-rootless --experimental
```

To deploy the TSan server, we also need to map the host port to the docker container port.
For example, assume we have an available Flask server running on the port 5000 in the container. The port 5030 on the host is assigned to the microservice. While creating the container, the port mapping is needed as follows.

```bash
docker pull racedetection/rds:tsan-server
docker run --rm -it -p 5030:5000 -d --link dind-server:docker racedetection/rds:tsan-server /flask/start.sh
```

Finally, on the host browser we can access the microservice at `127.0.0.1:5030`. For other external machine, it can be accessed at `<host_ip>:5030`.


