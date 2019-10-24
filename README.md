# kaldi-asr-aws
This code repo is in reference to the Medium Article for setting up Kaldi on AWS

*/1 * * * * sh ~/getConvertAudios.sh
*/2 * * * * sh ~/uploadOutput.sh



docker run -d -it --name kaldi -v ~/models:/models/ -v ~/audiosKaldi/processing:/audios/ -v ~/output:/output/ kaldi bash


docker exec -it kaldi bash



/home/ec2-user/
-aduios
-audiosKaldi
-kaldi Dock
-models .zip , tm, tw
-output
ffmpeg
getConv
uploadO
