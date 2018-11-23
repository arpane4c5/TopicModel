#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:22:55 2018

@author: Arpan
@Description: HMDB51 Experimental setup.

"""

import os
import numpy as np
import pandas as pd


def read_from_split_file(split_filepath):
    """
    Take the path of the splits_file, read the lines and get the training set
    and test set videos.
    -----
    Parameters:
    split_filepath: str
        complete path to single splits file.
    
    Return:
        trainSet: list of str
        testSet: list of str
        
    """    
    with open(split_filepath, 'r') as f:
        lines = f.read().splitlines()
    splits = [(l.split(' ')[0], l.split(' ')[1]) for l in lines]
    #print(lines)
    trainSet = [vName for (vName, part) in splits if part=='1']
    testSet = [vName for (vName, part) in splits if part=='2']
    return trainSet, testSet


def get_train_test_splits(DATASET, SPLITS, split_id=1):
    """
    Read the splits txt files present in the folder (corresponding to id), and
    get the training and testing video filenames and paths in separate lists.
    
    Parameters:
    ------
    DATASET: str
        path containing 51 folders each with its set of videos.
    SPLITS: str
        path containing 153 txt files with train/test split info.
    split_id: int
        which split to select (can be 1, 2 or 3)
    
    Returns:
    ------
    train_filenames: list of str
        3570 training filepaths (each of the form <folder/file.avi>)
    test_filenames: list of str
        1530 testing video filepaths.
    """
    print("Reading file paths for split {}...".format(split_id))
    #classes = os.listdir(DATASET)
    split_files = os.listdir(SPLITS)
    
    # get the split files corresponding to only split_id
    split = [sf for sf in split_files if sf.rsplit('.')[0][-1]==str(split_id)]
    
    train_filenames = []
    test_filenames = []
    
    split_classes = [fname.split('_test_')[0] for fname in split]
    # Iterate over that particular splits' files 
    for i, fname in enumerate(split):
        split_file = os.path.join(SPLITS, fname)
        trSet, testSet = read_from_split_file(split_file)
        trSet = [os.path.join(split_classes[i], f) for f in trSet]
        testSet = [os.path.join(split_classes[i], f) for f in testSet]
        train_filenames.extend(trSet)
        test_filenames.extend(testSet)
    
    # verify that files exist at the path.
    for f in train_filenames:
        assert os.path.exists(os.path.join(DATASET, f)), "File does not exist! "+f
    for f in test_filenames:
        assert os.path.exists(os.path.join(DATASET, f)), "File does not exist! "+f                         
    
    return train_filenames, test_filenames
#    print("Train Set :: ")
#    print(len(train_filenames))
#    print("Test Set :: ")
#    print(len(test_filenames))
