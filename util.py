import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def load_artifacts():
    print("Loading saved artifacts")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    with open("./artifacts/Aashiyan.pickle","rb") as f:
        __model =pickle.load(f)
    print("Artifacts loaded")




def get_locations():
    load_artifacts()
    return __locations

def get_price(loc,sqft,bhk,bath):
    load_artifacts()
    try:
      loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)




    return __model.predict([x])





if __name__=="__main__":
    load_artifacts()
    print(get_price("giri nagar",1000,3,3))