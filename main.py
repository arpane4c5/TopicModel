#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 01:28:56 2018

@author: Arpan

@Description: Unsupervised action recognition in HMDB51 dataset using Topic Modeling.
This file is the top level file that call other functions.

"""

import torch
import cv2
import numpy as np
import os
import pandas as pd
import argparse
import utils



def main(DATASET, SPLITS):
    
    print("DATASET: ", DATASET)
    print("DATASET: ", SPLITS)
    
    for i in range(3):
        train, test = utils.get_train_test_splits(DATASET, SPLITS, split_id=(i+1))
        
        # train models
        
        # evaluate on test
        
    print("Done")
    


if __name__ == '__main__':


    #Server Params
    DATASETBASE = "/home/arpan/DATA_Drive2/video_datasets/hmdb51"

    # Local Params
    if os.path.exists("/home/hadoop/VisionWorkspace/VideoData"):
        DATASETBASE = "/home/hadoop/VisionWorkspace/VideoData/hmdb51"

    DATASET = os.path.join(DATASETBASE, "videos")
    SPLITS = os.path.join(DATASETBASE, "train_test_splits")
    
    
    description = "Script for taking HMDB51 videos and extracting features from it."
    p = argparse.ArgumentParser(description=description)
    
    p.add_argument('-ds', '--DATASET', type=str, default=DATASET,
                   help=('input directory containing input video folders'))
    p.add_argument('-sp', '--SPLITS', type=str, default=SPLITS,
                   help=('input directory containing train test splits'))
    
#    p.add_argument('-w', '--SEQ_SIZE', type=int, default=SEQ_SIZE)
#    p.add_argument('-b', '--BATCH_SIZE', type=int, default=BATCH_SIZE)
#    p.add_argument('-hs', '--HIDDEN_SIZE', type=int, default=HIDDEN_SIZE)
#    p.add_argument('-n', '--N_EPOCHS', type=int, default=N_EPOCHS)
#    p.add_argument('-l', '--N_LAYERS', type=int, default=N_LAYERS)    
#    p.add_argument('-t', '--threshold', type=int, default=threshold)
#    p.add_argument('-s', '--seq_threshold', type=int, default=seq_threshold)
#    p.add_argument('-g', '--use_gpu', type=bool, default=use_gpu)
    
    
    #for seq in range(32, 35):
        #p.set_defaults(SEQ_SIZE = seq)
    tiou = main(**vars(p.parse_args()))
    

    
    

    
    # Read the sequences from the txt file.
    #import kth_read_sequences as sequences
    
    #labels = sequences.read_sequences_file(KTH_SEQ)
    
    # First apply to text models
    
    
    # Call the feature extraction method
    
    
    # Apply LDA, Train model
    
    
    # Apply trained model on the extracted features of the validation set.
    
    
    # Evaluate




