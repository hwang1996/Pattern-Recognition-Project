#!/usr/bin/env sh

export PYTHONPATH='/data6/wanghao/pattern_recognition_project/net'

G_logtostderr=1 /data5/wanghao/caffe/build/tools/caffe train \
   --solver=/data6/wanghao/pattern_recognition_project/net/solver.prototxt \
   --gpu=0 2>&1 |tee /data6/wanghao/pattern_recognition_project/net/out.log
