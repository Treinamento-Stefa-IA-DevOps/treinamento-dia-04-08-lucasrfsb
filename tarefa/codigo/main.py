import pickle
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo

def titanic(Sex:int, Age:float, Lifeboat: int,Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

        data = [[Age, Lifeboat, Pclass, Sex]] ## from inspect_pickle.py discovered that inputs are sorted

        df = pd.DataFrame(data, columns = ['Age', 'Lifeboat', 'Pclass', 'Sex']) ## Rename to expected labeled columns
        y = titanic.predict(df)

        ans = bool(y[0])

        return {
            "survived": ans,
            "status": 200,	
            "message": "Passenger Survived" if ans else "Passenger Died",	
        }


@app.get('/model')
def get():
    return {'hello':'test'}
