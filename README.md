# kaldi-asr-aws
This code repo is in reference to the [Medium Article](https://medium.com/@mrpuri/automatic-speech-recognition-as-a-microservice-on-aws-6da646631fdb "Medium Article") for setting up Kaldi on AWS

- **Kaldi** => Dockerfile
- **bash** => Contains all the shell scripts
- **flask-app** => Python code and HTML file
- **lambda** => Python code for two lambda functions

## Directory Structure Tree

    D -> Represents Directory
    F -> Represents File
    cd /home/ec2-user/
      -audios D [ Files from S3 will be synced here ]
      -audiosKaldi D 
        -processing D [ Files ready for Transcription are moved here ]
        -sendWavToProcess.sh F
      -kaldi D
        -Dockerfile F
      -models D
        -model.zip F (unzip here)
        -transcriptMaster.sh F
        -transcriptWorker.sh F
      -output D [ Transcription in .txt file will be store here]
      ffmpeg F
      getConvertAudios.sh F
      uploadOutput.sh F

#### - Kaldi
Build the Kaldi container using Dockerfile

    cd /path/to/Dockerfile
    docker build -t kaldi .

Starting the container

    docker run -d -it --name kaldi -v ~/models:/models/ -v ~/audiosKaldi/processing:/audios/ -v ~/output:/output/ kaldi bash

Entering into the container

    docker exec -it kaldi bash

#### - Bash Scripts

- **getConvertAudios.sh** -> This script syncs files from S3 into audios/ directory and using ffmpeg converted and stored into audiosKaldi/
- **uploadOutput.sh** -> This script syncs the .txt files in output/ directory into S3 bucket
- **sendWavToProcess.sh** -> This script limits the number of files for processing to the number of cores on the VM for parallel processing
- **transcriptMaster.sh** -> This script calls transcriptWorker.sh for every audio file placed in the processing folder and ensures at any time only #no. of cores amount of files are running
- **transcriptWorker.sh** -> Where the magic happens, actual transcription happens through this file.

#### - Flask App
Installation/Setup

    sudo yum install python2-pip.noarch
    sudo pip install virtualenv
    virtualenv /path/to/some/directory
    source /path/to/some/directory/bin/activate
    pip install flask boto3 requests
    ###### Copy the flask-app files into - /path/to/some/directory
    cd /path/to/some/directory
    python app.py &


#### - Lambda
Refer Medium Article

#### - ffmpeg
Download **ffmpeg-release-amd64-static.tar.xz - md5** from [here](https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz "here")

#### - Kaldi Model
Download model.zip from here - https://crossregionreplpuri.s3.ap-south-1.amazonaws.com/model.zip
