'''
TABULAR DATA -- FEATURE EXTRACTION
The pyAudioAnalysis has two functions in order to extract a bunch of useful
features from a wav file.
'''

from pyAudioAnalysis import MidTermFeatures as mF
import numpy as np
import pandas as pd
import os
basepath1 = 'D:/GitHub/Roldo/Cough dataset/'

TYPE=['TRAIN','TEST']
for t in TYPE:
    basepath_train_cough = basepath1+'Unlabeled audio/'+t+'/Cough/'
    basepath_train_nocough = basepath1+'Unlabeled audio/'+t+'/No_Cough/'


    [mid_term_features_cough, wav_file_list_cough, mid_feature_names] =  mF.directory_feature_extraction(basepath_train_cough, 0.1,0.1, 0.01, 0.01, compute_beat=False)
    [mid_term_features_nocough, wav_file_list_nocough, mid_feature_names] =  mF.directory_feature_extraction(basepath_train_nocough, 0.1,0.1, 0.01, 0.01, compute_beat=False)

    label_nocough = np.zeros(np.shape(mid_term_features_nocough)[0])
    label_cough = np.ones(np.shape(mid_term_features_cough)[0])

    features = np.concatenate((mid_term_features_cough, mid_term_features_nocough))  # Equivalent to rbind() in R
    labels = np.concatenate((label_cough, label_nocough))
    mid_feature_names = np.array(mid_feature_names)

    filenames_cough = []
    for i in range(len(wav_file_list_cough)):
        filenames_cough.append(os.path.split(os.path.abspath(wav_file_list_cough[i]))[1].split('.')[0])

    filenames_nocough = []
    for i in range(len(wav_file_list_nocough)):
        filenames_nocough.append(os.path.split(os.path.abspath(wav_file_list_nocough[i]))[1].split('.')[0])

    filenames = np.concatenate((filenames_cough, filenames_nocough))

    df = pd.DataFrame(features, columns = mid_feature_names)
    df['Label'] = pd.Series(labels)
    df['Filenames'] = pd.Series(filenames)


    df.to_excel(basepath1+'Unlabeled audio/'+t+'/features_extracted_'+t+'.xlsx', index=False, header=True)
    df.to_json(basepath1+'Unlabeled audio/'+t+'/features_extracted_'+t+'.json')


    '''
    Let's extract the features from some Positive cough audios.
    We know in advance that some Cough-Shallow audios have too short duration
    '''

import soundfile as sf
for t in TYPE:

    #basepath2 = basepath1+'Labeled audio/'+t+'/'
    basepath_pos = basepath1+'Labeled audio/'+t+'/Pos/'
    basepath_neg = basepath1+'Labeled audio/'+t+'/Neg/'
    
    [mid_term_features_pos, wav_file_list_pos, mid_feature_names] =  mF.directory_feature_extraction(basepath_pos, 0.1,0.1, 0.01, 0.01, compute_beat=False)
    [mid_term_features_neg, wav_file_list_neg, mid_feature_names] =  mF.directory_feature_extraction(basepath_neg, 0.1,0.1, 0.01, 0.01, compute_beat=False)

    label_neg = np.zeros(np.shape(mid_term_features_neg)[0])
    label_pos = np.ones(np.shape(mid_term_features_pos)[0])

    features = np.concatenate((mid_term_features_pos, mid_term_features_neg))  # Equivalent to rbind() in R
    labels = np.concatenate((label_pos, label_neg))
    mid_feature_names = np.array(mid_feature_names)

    filenames_pos = []
    for i in range(len(wav_file_list_pos)):
        filenames_pos.append(os.path.split(os.path.abspath(wav_file_list_pos[i]))[1].split('.')[0])

    filenames_neg = []
    for i in range(len(wav_file_list_neg)):
        filenames_neg.append(os.path.split(os.path.abspath(wav_file_list_neg[i]))[1].split('.')[0])

    filenames = np.concatenate((filenames_pos, filenames_neg))

    df = pd.DataFrame(features, columns = mid_feature_names)
    df['Label'] = pd.Series(labels)
    df['Filenames'] = pd.Series(filenames)


    df.to_excel(basepath1+'Labeled audio/'+t+'/features_extracted_'+t+'.xlsx', index=False, header=True)
    df.to_json(basepath1+'Labeled audio/'+t+'/features_extracted_'+t+'.json')
    #---------------------------