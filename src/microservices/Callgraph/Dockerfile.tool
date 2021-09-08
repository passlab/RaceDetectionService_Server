
# Environment for the microservice Archer.
# Clang 6 is compiled from source.
# ninja check-libarcher is not working yet, but clang-archer can run.

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
        cmake \
        curl \
        dialog \
        g++ \
        gcc \
        gdb \
        git \
        ninja-build \
        python3-dev \
        software-properties-common \
        time \
        vim \
        wget && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/*

# Build LLVM

ENV ARCHER_BUILD /opt/ArcherBuild


RUN mkdir -p $ARCHER_BUILD && \
    cd $ARCHER_BUILD && \
    git clone https://github.com/llvm-mirror/llvm.git llvm_src && \
    cd llvm_src && \
    git checkout release_60 && \
    cd tools && \
    git clone https://github.com/llvm-mirror/clang.git clang && \
    cd clang && \
    git checkout release_60 && \
    cd .. && \
    git clone https://github.com/PRUNERS/archer.git archer && \
    cd .. && \
    cd projects && \
    git clone https://github.com/llvm-mirror/compiler-rt.git compiler-rt && \
    cd compiler-rt && \
    git checkout release_60 && \
    cd .. && \
    git clone https://github.com/llvm-mirror/libcxx.git && \
    cd libcxx && \
    git checkout release_60 && \
    cd .. && \
    git clone https://github.com/llvm-mirror/libcxxabi.git && \
    cd libcxxabi && \
    git checkout release_60 && \
    cd .. && \
    git clone https://github.com/llvm-mirror/libunwind.git && \
    cd libunwind && \
    git checkout release_60 && \
    cd .. && \
    git clone https://github.com/llvm-mirror/openmp.git openmp && \
    cd openmp && \
    git checkout release_60

#ENV CC $(which gcc)
#ENV CXX $(which g++)

RUN cd $ARCHER_BUILD && \
    mkdir -p llvm_bootstrap && \
    cd llvm_bootstrap && \
    cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_TOOL_ARCHER_BUILD=OFF \
    -DLLVM_TARGETS_TO_BUILD=Native \
    ../llvm_src && \
    ninja -j2 -l2 && \
    cd ..

ENV LD_LIBRARY_PATH $ARCHER_BUILD/llvm_bootstrap/lib:${LD_LIBRARY_PATH}
ENV PATH $ARCHER_BUILD/llvm_bootstrap/bin:${PATH}
ENV LLVM_INSTALL /opt/llvm_install

# -D CLANG_DEFAULT_OPENMP_RUNTIME:STRING=libomp \
RUN cd $ARCHER_BUILD && \
    mkdir llvm_build && cd llvm_build && \
    cmake -G Ninja \
    -D CMAKE_C_COMPILER=clang \
    -D CMAKE_CXX_COMPILER=clang++ \
    -D CMAKE_BUILD_TYPE=Release \
    -D OMP_PREFIX:PATH=$LLVM_INSTALL \
    -D OMP_LIB_PATH=$ARCHER_BUILD/llvm_bootstrap/lib \
    -D CMAKE_INSTALL_PREFIX:PATH=$LLVM_INSTALL \
    -D LLVM_ENABLE_LIBCXX=ON \
    -D LLVM_ENABLE_LIBCXXABI=ON \
    -D LIBCXXABI_USE_LLVM_UNWINDER=ON \
    -D CLANG_DEFAULT_CXX_STDLIB=libc++ \
    -D LIBOMP_OMPT_SUPPORT=on \
    -D LIBOMP_OMPT_BLAME=on \
    -D LIBOMP_OMPT_TRACE=on \
    ../llvm_src && \
    ninja -j2 -l2

RUN cd $ARCHER_BUILD && \
    cd llvm_build && \
    ninja install

   # ninja check-libarcher && \
ENV PATH ${LLVM_INSTALL}/bin:${PATH}
ENV LD_LIBRARY_PATH ${LLVM_INSTALL}/lib:${LD_LIBRARY_PATH}

# Setup environment.
ENV CC $LLVM_PATH/bin/clang
ENV CXX $LLVM_PATH/bin/clang++

COPY --chown=rds:rds [".bashrc", "/home/rds/"]
COPY --chown=rds:rds ["run.sh", "/home/rds/"]

# Switch user and working directory.
USER rds
WORKDIR /home/rds

# Use dataracebench as a wrapper to perform detection
RUN git clone https://github.com/RaceDetectionService/dataracebench.git && \
    rm -rf /home/rds/dataracebench/micro-benchmarks/* && \
    rm -rf /home/rds/dataracebench/results/*

# Define default command.
CMD ["bash"]
