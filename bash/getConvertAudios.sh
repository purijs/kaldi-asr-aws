#!/bin/bash

aws s3 sync s3://<BUCKET_NAME>/incoming ~/audios/ --include "*.wav" --include "*.mp3" --delete

for audio in $(find /home/ec2-user/audios/ -type f)
do
        filename_noext=$(basename $audio | cut -f 1 -d '.')
        /home/ec2-user/ffmpeg -i $audio -ar 8000 ~/audiosKaldi/$filename_noext.wav
        rm -rf $audio
done
aws s3 sync ~/audios/ s3://<BUCKET_NAME>/incoming --include "*.wav" --include "*.mp3" --delete
