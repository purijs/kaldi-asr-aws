#!/bin/bash

audio_name=$2

/opt/kaldi/src/online2bin/online2-wav-nnet3-latgen-faster --online=true --do-endpointing=false --frame-subsampling-factor=3 --config=/models/conf/online.conf --max-active=10000 --beam=30.0 --lattice-beam=6.0 --acoustic-scale=1.0 --word-symbol-table=/models/exp/tdnn_7b_chain_online/graph_pp/words.txt /models/exp/chain/tdnn_7b/final.mdl /models/exp/tdnn_7b_chain_online/graph_pp/HCLG.fst 'ark:echo utterance-id1 utterance-id1|' "scp:echo utterance-id1 '$1'|" "ark:|gzip -c > /dev/null" 2>&1 | tee /output/$audio_name.temp

checkFailure=$(cat /output/$audio_name.temp | grep "Stack-Trace")

if [ $? -eq 0 ]; then
    echo 'error' > /output/$audio_name.txt
    exit 0
fi

cat /output/$audio_name.temp | grep utterance-id1 | grep -v LOG | grep -v online2-wav-nnet3-latgen-faster > /output/$audio_name.txt

rm -rf /output/$audio_name.temp

rm -rf $1
