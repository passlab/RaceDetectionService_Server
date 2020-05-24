
# Environment for the microservice ROMP.

# Pull base image.
FROM ubuntu:18.04

# Add user
RUN groupadd -g 9999 rds && \
    useradd -r -u 9999 -g rds -m -d /home/rds rds

# Install packages.
RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        bc \
        build-essential \
        clang \
        cmake \
        curl \
        dialog \
        g++ \
        gcc \
        gdb \
        git \
        python3-dev \
        software-properties-common \
        time \
        vim \
        wget && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/*

# Add user
RUN useradd -r -u 9990 -g rds -m -d /home/awang15 awang15

COPY --chown=rds:rds [".spack", "/home/awang15/.spack"]
COPY --chown=rds:rds ["spack", "/home/awang15/Projects/romp/spack"]

COPY --chown=rds:rds [".bashrc", "/home/rds/"]
COPY --chown=rds:rds ["run.sh", "/home/rds/"]

# Switch user and working directory.
USER rds
WORKDIR /home/rds
ENV PATH /home/awang15/Projects/romp/spack/bin:$PATH

# Use dataracebench as a wrapper to perform detection
RUN git clone https://github.com/RaceDetectionService/dataracebench.git && \
    rm -rf /home/rds/dataracebench/micro-benchmarks/* && \
    rm -rf /home/rds/dataracebench/results/*

# Define default command.
CMD ["bash"]
