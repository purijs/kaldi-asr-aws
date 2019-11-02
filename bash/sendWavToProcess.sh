#!/bin/bash

while true; do

        filesToProcessCount=$(ls ~/audiosKaldi/*.wav | wc -l)
        filesInProcessCount=$(ls ~/audiosKaldi/processing/*.wav | wc -l)

        cores=$(nproc)

        if [ $filesInProcessCount -lt $cores ]; then

                canProcess=$(($cores - $filesInProcessCount))

                for audio in $(find ~/audiosKaldi/*.wav -type f | head -$canProcess)
                        do

                                mv $audio ~/audiosKaldi/processing/

                        done

        fi

        sleep 30

done
