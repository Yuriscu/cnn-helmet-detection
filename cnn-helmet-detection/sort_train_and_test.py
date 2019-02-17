import os
import shutil

neg_files = os.listdir("negative")
pos_files = os.listdir("positive")

neg = len(neg_files)
pos = len(pos_files)

#%80 train %20 test for negative images
neg_train = int(neg * 0.8)
neg_test = neg - neg_train
#%80 train %20 test for positive images
pos_train = int(pos * 0.8)
pos_test = pos - pos_train

os.makedirs('train/negative')
os.makedirs('train/positive')
os.makedirs('test/negative')
os.makedirs('test/positive')

for i in range(0, neg_train):
    file = "neg/" + neg_files[i]
    shutil.move(file, "train/negative")
    
for i in range(neg_train, neg):
    file = "neg/" + neg_files[i]
    shutil.move(file, "test/negative")
    
for i in range(0, pos_train):
    file = "pos/" + pos_files[i]
    shutil.move(file, "train/positive")
    
for i in range(pos_train, pos):
    file = "pos/" + pos_files[i]
    shutil.move(file, "test/positive")
