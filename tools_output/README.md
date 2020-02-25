## Tools

1. To install inspector:

	```	
	Download inspector for linux from Intel inspector website: https://software.intel.com/en-us/inspector/choose-download
	tar -czvf inspector_2019_update5.tar.gz
	cd inspector_2019_update5
	sudo ./install.sh
	Download parallel_studio_xe_2020_cluster_edition from Intel
	install parallel_studio
	export PATH=/opt/intel/parallel_studio_xe_2020.0.088/bin/psxevars.sh:$PATH
	export PATH=/opt/intel/bin:$PATH
	export PATH=/opt/intel/inspector/bin32:$PATH
	
	
	
1. The command line to use inspector:

	```	
	export OMP_NUM_THREADS=5
	icc -O0 -g -fopenmp DRB001-antidep1-orig-yes.c -o myApp
	inspxe-cl  -collect ti3 -knob scope=extreme -knob stack-depth=16 -knob use-maximum-resources=true -result-dir myResult ./myApp
	inspxe-cl -create-suppression-file ./mySupFile -result-dir Result
	inspxe-cl -report problems -result-dir Result -report-output Result/myThreadingReport.txt

   Check the report to see whether you can locate the binary address of a datarace and then use `addr2line` to locate line number in the source code. 

1. To install ThreadSanitizer:

	```	
	wget https://releases.llvm.org/10.0.0/llvm-10.0.0.src.tar.xz
 	wget https://releases.llvm.org/10.0.0/cfe-10.0.0.src.tar.xz
 	wget https://releases.llvm.org/10.0.0/openmp-10.0.0.src.tar.xz
	wget https://releases.llvm.org/10.0.0/compiler-rt-10.0.0.src.tar.xz
 	tar xf llvm-10.0.0.src.tar.xz
	tar xf cfe-10.0.0.src.tar.xz
	tar xf openmp-10.0.0.src.tar.xz
	tar xf compiler-rt-10.0.0.src.tar.xz
	mv cfe-10.0.0.src llvm-10.0.0.src/tools/clang
	mv openmp-10.0.0.src llvm-10.0.0.src/projects/openmp
	mv compiler-rt-10.0.0.src llvm-10.0.0.src/projects/compiler-rt
	mkdir build
 	cd build
	cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$(pwd)/../install \
	-DCLANG_OPENMP_NVPTX_DEFAULT_ARCH=sm_60 \
	-DLIBOMPTARGET_NVPTX_COMPUTE_CAPABILITIES=35,60,70 ../llvm-10.0.0.src
	make -j8
	make -j8 install
	cd ..
	mkdir build-openmp
	cd build-openmp
	 cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$(pwd)/../install \
	-DCMAKE_C_COMPILER=$(pwd)/../install/bin/clang \
	-DCMAKE_CXX_COMPILER=$(pwd)/../install/bin/clang++ \
	-DLIBOMPTARGET_NVPTX_COMPUTE_CAPABILITIES=35,60,70 \
	../llvm-10.0.0.src/projects/openmp
	make -j8
	make -j8 install
	cd ..
	export PATH=$(pwd)/install/bin:$PATH
 	export LD_LIBRARY_PATH=$(pwd)/install/lib:$LD_LIBRARY_PATH

1. The command line to use ThreadSanitizer:
 
 	```	
	clang DRB001-antidep1-orig-yes.c -fopenmp -fsanitize=thread -fPIE -pie -g -o myApp
	./myApp 

1. To install Archer:
 
 	```	
 	export ARCHER_BUILD=$PWD/ArcherBuild
	mkdir $ARCHER_BUILD && cd $ARCHER_BUILD
	git clone https://github.com/llvm-mirror/llvm.git llvm_src
	cd llvm_src
	git checkout release_60
	cd tools
	git clone https://github.com/llvm-mirror/clang.git clang
	cd clang
	git checkout release_60
	cd ..
	git clone https://github.com/PRUNERS/archer.git archer
	cd ..
	cd projects
	git clone https://github.com/llvm-mirror/compiler-rt.git compiler-rt
	cd compiler-rt
	git checkout release_60
	cd ..
	git clone https://github.com/llvm-mirror/libcxx.git
	cd libcxx
	git checkout release_60
	cd ..	
	git clone https://github.com/llvm-mirror/libcxxabi.git
	cd libcxxabi
	git checkout release_60
	cd ..
	git clone https://github.com/llvm-mirror/libunwind.git
	cd libunwind
	git checkout release_60
	cd ..
	git clone https://github.com/llvm-mirror/openmp.git openmp
	cd openmp
	git checkout release_60
	cd $ARCHER_BUILD
	mkdir -p llvm_bootstrap
	cd llvm_bootstrap
	sudo apt install ninja-build
	CC=$(which gcc) CXX=$(which g++) cmake -G Ninja \
	 -DCMAKE_BUILD_TYPE=Release \
	 -DLLVM_TOOL_ARCHER_BUILD=OFF \
	 -DLLVM_TARGETS_TO_BUILD=Native \
	 ../llvm_src
	ninja -j12 -l12
	cd ..
	export LD_LIBRARY_PATH="$ARCHER_BUILD/llvm_bootstrap/lib:${LD_LIBRARY_PATH}"
	export PATH="$ARCHER_BUILD/llvm_bootstrap/bin:${PATH}"
	export LLVM_INSTALL=$HOME/usr
	mkdir llvm_build && cd llvm_build
	cmake -G Ninja \
	 -D CMAKE_C_COMPILER=clang \
	 -D CMAKE_CXX_COMPILER=clang++ \
	 -D CMAKE_BUILD_TYPE=Release \
	 -D OMP_PREFIX:PATH=$LLVM_INSTALL \
	 -D CMAKE_INSTALL_PREFIX:PATH=$LLVM_INSTALL \
	 -D CLANG_DEFAULT_OPENMP_RUNTIME:STRING=libomp \
	 -D LLVM_ENABLE_LIBCXX=ON \
	 -D LLVM_ENABLE_LIBCXXABI=ON \
	 -D LIBCXXABI_USE_LLVM_UNWINDER=ON \
	 -D CLANG_DEFAULT_CXX_STDLIB=libc++ \
	 -D LIBOMP_OMPT_SUPPORT=on \
	 -D LIBOMP_OMPT_BLAME=on \
	 -D LIBOMP_OMPT_TRACE=on \
	 ../llvm_src
	ninja -j12 -l12
	ninja check-libarcher
	ninja install
	export PATH=${LLVM_INSTALL}/bin:${PATH}"
	export LD_LIBRARY_PATH=${LLVM_INSTALL}/lib:${LD_LIBRARY_PATH}"

1. The command line to use Archer:
 
 	```	
 	clang-archer DRB104-nowait-barrier-orig-no.c -o myApp -larcher
	./myApp 
	
1. The command line to use python parser:
 
 	```	
 	python3 outputParser.py [your file name(Tsan.txt)] >output.txt
	 
