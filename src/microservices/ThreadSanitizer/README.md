
# Deployment

### Prerequisite

1. OS:
Ubuntu 18.04

1. Install docker
```bash
sudo apt update
sudo apt install docker.io
```

### Get the docker image

```bash
sudo docker pull ouankou/rds:threadsanitizer
```
### Create a container

```bash
sudo docker run -it --name rds_tsan ouankou/rds:threadsanitizer bash
```

### Start a container

```bash
sudo docker start rds_tsan
```

### Enter a container

```bash
sudo docker exec -it rds_tsan bash
```

### ThreadSanitizer usage

Follow the official guide or other instructions.

https://clang.llvm.org/docs/ThreadSanitizer.html
