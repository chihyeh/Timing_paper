#!/bin/bash

echo "Set enviroment for this program"

export ROOTSYS=/share/cern/root
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$ROOTSYS/lib:$PYTHONPATH
export PATH=.:$PATH
GOODRUN=`pwd`/GoodRuns/StandAlone/
export LD_LIBRARY_PATH=$GOODRUN:$LD_LIBRARY_PATH
export FASTJET=`pwd`/fastjet
export LD_LIBRARY_PATH=$FASTJET/src/lib:$LD_LIBRARY_PATH
export TRIGJET=`pwd`/TrigRootAnalysis/standalone/
export LD_LIBRARY_PATH=$TRIGJET/src/lib:$LD_LIBRARY_PATH

export LD_LIBRARY_PATH=/users/reb/texlive/2012/bin/x86_64-linux/:$LD_LIBRARY_PATH
export PATH=/users/reb/texlive/2012/bin/x86_64-linux/:$PATH

