
"""
Omkar Thawakar , Sachin Chaoudhary
CVPR Lab IIT Ropar

Following code prepare custom data (HMDB51) for training of Non Local Neural Network tensorflow.

"""

import os
import glob
import numpy as np
from PIL import Image

split_data = {}
for file in sorted(glob.glob('''  path for txt files which contains train test annotations in HMDB51   ''')):
    with open(file) as f:
        for line in f:
            split_data[line.split(' ')[0].split('.')[0]] = int(line.split(' ')[1])


location = 'Path_to_HMDB_dataset'
train_data , train_labels = [],[]
test_data , test_labels = [],[]
val_data , val_labels = [],[]
clasess = []
labels = {}
for foldername in sorted(os.listdir(location)):
    clasess.append(foldername)
for i in range(len(clasess)):
    tmp = np.zeros(len(clasess),dtype=np.int32)
    tmp [i] = 1
    labels[clasess[i]]=tmp


for video in clasess:
    for videoname in sorted(glob.glob(location+video+'/*')):
        print(videoname.split('/')[-1])
        print(video)
        print('='*50)
        if split_data[videoname.split('/')[-1]] == 1 :
            for img in sorted(glob.glob(videoname+'/*')):
                print('processing!!',end='\r')
                image = Image.open(img)
                image = image.resize((240,320), Image.ANTIALIAS)
                tmp = np.asarray(image)
                train_data.append(tmp)
                train_labels.append(labels[video])
                
        elif split_data[videoname.split('/')[-1]] == 2 :
            for img in sorted(glob.glob(videoname+'/*')):
                print('processing!!',end='\r')
                image = Image.open(img)
                image = image.resize((240,320), Image.ANTIALIAS)
                tmp = np.asarray(image)
                test_data.append(tmp)
                test_labels.append(labels[video]) 
        
        elif split_data[videoname.split('/')[-1]] == 0 :
            for img in sorted(glob.glob(videoname+'/*')):
                print('processing!!',end='\r')
                image = Image.open(img)
                image = image.resize((240,320), Image.ANTIALIAS)
                tmp = np.asarray(image)
                val_data.append(tmp)
                val_labels.append(labels[video])

                           
np.savetxt('train_data.txt',np.array(train_data))
np.savetxt('train_labels.txt',np.array(train_labels))


np.savetxt('test_data.txt',np.array(test_data))
np.savetxt('test_labels.txt',np.array(test_labels))


np.savetxt('val_data.txt',np.array(val_data))
np.savetxt('val_labels.txt',np.array(val_labels))

