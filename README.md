# HMDB51 data generation for training of Non Local Neural Network
Requirement
```
PIL
numpy
cv2
glob
```

HMDB51 datset folder contains following actions and each action contains different videos
```
----HMDB51
        |-brush_hair
                  |-April_09_brush_hair_u_nm_np1_ba_goo_0.avi
                  .....
                  |-Slave_brush_my_hair_brush_hair_u_cm_np2_le_goo_2.avi
        |-cartwheel
                  |-
                  .....
                  |-
        
        |-catch
                  |-
                  .....
                  |-
        
        |-.......
        |-wave
                  |-21_wave_u_nm_np1_fr_goo_5.avi
                  .....
                  |-
                  


```
To extract frames from each HMDB51 actions run following code
```
python frameExtract.py
```
To create train test split we require annotation of each video in actionset which is found in splits folder downloaded from 
[HMDB51](http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#overview)

Train_Test split file contains following structure
```
----splits
        |-brush_hair_test_split1.txt
        |-brush_hair_test_split2.txt
        |-brush_hair_test_split3.txt
        |-cartwheel_test_split1.txt
        |-.......
        |-.......
        |- 
        |-action_name_test_split{}.txt

```
For getting train test splits run following code
```
python create_train_test_split.py
```
Above script takes about an hour to read whole dataset and saves train,test and validation data in following files respectively.
```
---|-train_data.txt
   |-train_labels.txt
   |-test_data.txt
   |-test_labels.txt
   |-val_data.txt
   |-val_labels.txt
```
For furthur use load train,test and val data directly by running
```
np.loadtxt('train_data.txt')
```


