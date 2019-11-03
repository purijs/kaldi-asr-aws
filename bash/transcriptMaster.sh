#!/bin/bash

chmod 777 -R /audios/*

filesCount=$(ls /audios/*.wav | wc -l)

cores=$(nproc)

if [ $filesCount -eq 0 ]; then

        for audio in $(find /audios/*.wav -type f | head -$cores)
        do

                audio_name=$(basename $audio | cut -f 1 -d '.')
                /models/transcriptWorker.sh $audio $audio_name &

        done
fi
