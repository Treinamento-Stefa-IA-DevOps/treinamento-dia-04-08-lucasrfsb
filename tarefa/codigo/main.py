import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo

def titanic(Sex:int, Age:float, Lifeboat: int,Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    pred = titanic.predict([[Sex, Age, Lifeboat, Pclass]])    

    if(pred):
        return  {"survived": True,	"status": 200,	"message": "Sobreviveu" }
    else: 
        return {"survived": False,	"status": 200,	"message": "Morreu" }

@app.get('/model')
def get():
    return {'hello':'test'}

    
