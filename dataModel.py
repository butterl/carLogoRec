from PIL import Image
import numpy as np
import h5py
import re,os

pattern = ".+\.jpg"
trainPaths = [
    "./Cardata/train/0",
    "./Cardata/train/1",
    "./Cardata/train/2",
    "./Cardata/train/3",
    "./Cardata/train/4"
    ]
testPaths = [
    "./Cardata/test/0",
    "./Cardata/test/1",
    "./Cardata/test/2",
    "./Cardata/test/3",
    "./Cardata/test/4"
]




def create_dataset():
    '''
    Model the datasets

    train_X: (n_features, n_samples)
    train_Y: (1, n_samples)
    ...
    :return: None
    '''
    dataset = h5py.File('carDatasets.h5', 'w')
    # train data
    ## sample 1000
    ## size: resize to 45x45=2025
    train_X = np.zeros(shape=(1000, 45*45*3),dtype=float)
    train_Y = np.zeros(shape=(1, 1000),dtype=float)
    count = 0
    for trainpath in trainPaths:
        for img in [file for file in os.listdir(trainpath) if re.match(pattern,file)]:
            img_path = trainpath+os.sep+img
            img_obj = Image.open(img_path).convert('RGB').resize((45,45),Image.ANTIALIAS)
            img_array = np.array(img_obj, dtype=np.uint8).reshape((1,45*45*3))
            train_X[count]=img_array
            train_Y[0][count]=float(trainpath[-1])
            count+=1
    dataset.create_dataset('train_X', data=train_X.T)
    dataset.create_dataset('train_Y', data=train_Y)

    # test data
    ## sample 500
    ## size: resize to 45x45=2025
    test_X = np.zeros(shape=(500, 45*45*3),dtype=float)
    test_Y = np.zeros(shape=(1, 500),dtype=float)
    count = 0
    for testpath in testPaths:
        for img in [file for file in os.listdir(testpath) if re.match(pattern,file)]:
            img_path = testpath+os.sep+img
            img_obj = Image.open(img_path).convert('RGB').resize((45,45),Image.ANTIALIAS)
            img_array = np.array(img_obj, dtype=np.uint8).reshape((1,45*45*3))
            test_X[count]=img_array
            test_Y[0][count]=float(testpath[-1])
            count+=1
    dataset.create_dataset('test_X', data=test_X.T)
    dataset.create_dataset('test_Y', data=test_Y)
    dataset.close()

if __name__=='__main__':
    #create_dataset()
    f = h5py.File('carDatasets.h5','r')
    train_X = np.array(f['test_Y'][:])
    print(train_X)