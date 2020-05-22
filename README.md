## Introduction

RaceDetectionService, a cloud-based metaservice aimed at providing convenient and high quality data race detection for user's OpenMP codes. Our work present and experiment a new direction of creating and using software tools for parallel computing, which is to use service-oriented architecture, cloud-computing and standard APIs to enhance the interoperability of tools. 

## Deployment the RaceDetectionService(RDS) enviorment to use

  There two different ways to set up your RDS. You can set up RDS by yourslef on your local machine or you can set up RDS enviorment by our docker image (recommended). 

1. Set up RDS enviorment via your desktop or server.

   First, install four data race detection tools by following instruction.

      [Instruction for install four tools](InstallTool.md)
   
   Second, set up your four RDS Micorservices by following instruction.
    
      [Instruction for setup four RDS Micorservices](MicroserviceSetup.md)
     
   Last, set up your RDS Metaservice by following instruction.
    
      [Instruction for setup RDS Metaservice](MetaserviceSetup.md)

2. Set up RDS enviorment via docker

      [Instruction of local deployment](deployment.md)

## Authors

Yaying Shi, Anjia Wang, Yonghong Yan and Chunhua Liao 

## Contact

Please file issues to this git repo. Alternatively, you can contact Chunhua Liao: liao6@llnl.gov .

## Acknowledgement

This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344. Work on the design of the framework was supported by the U.S. DOE Advanced Scientific Computing Program (ASCR SC-21).
