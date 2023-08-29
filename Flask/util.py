import pickle
import numpy as np

__model=None
def prediction(Internships,Age, CGPA, hostel, hob, branch):

    if (branch == 'Computer_Science'):
        Computer_Science = 1
        Electronics_And_Communication = 0
        Information_Technology = 0
        Mechanical = 0
        Electrical = 0
        Civil = 0
        
    elif (branch == 'Electronics_And_Communication'):
        Computer_Science = 0
        Electronics_And_Communication = 1
        Computer_Science = 1
        Information_Technology = 0
        Mechanical = 0
        Electrical = 0
        Civil = 0
    
    elif (branch == 'Information_Technology'):
        Computer_Science = 0
        Electronics_And_Communication = 0
        Information_Technology = 1
        Mechanical = 0
        Electrical = 0
        Civil = 0

    elif (branch == 'Mechanical'):
        Computer_Science = 0
        Electronics_And_Communication = 0
        Information_Technology = 0
        Mechanical = 1
        Electrical = 0
        Civil = 0

    elif (branch == 'Electrical'):
        Computer_Science = 0
        Electronics_And_Communication =0
        Information_Technology = 0
        Mechanical = 0
        Electrical = 1
        Civil = 0


    else:
        Computer_Science = 0
        Electronics_And_Communication = 0
        Information_Technology = 0
        Mechanical = 0
        Electrical = 0
        Civil = 1
            
           
    branchs=[Electronics_And_Communication,Computer_Science,Information_Technology,Mechanical,Electrical]
    x=[]
    x.append(Age)
    x.append(Internships)
    x.append(CGPA)
    x.append(hostel)
    x.append(hob)
    for i in branchs:
        x.append(i)
    print(x)
    return (__model.predict([x])[0])

def load_artifacts():
    global __model
    with open("model_pickle_modified",'rb') as f:
        __model=pickle.load(f)
    print("arti facts are loaded successfully ...")
if __name__ =='__main__':
    load_artifacts()
    print(__model.predict([[22, 1, 7, 0, 1, 0, 0, 0, 0, 0]]))