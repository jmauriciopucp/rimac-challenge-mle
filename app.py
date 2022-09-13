from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel, Field
import pandas as pd

#load the model
lgbm_clf = load(open('./model/lgbm_model.pkl','rb'))

#FastAPI instance
app = FastAPI()

class Item(BaseModel):
    age: int = Field(example=41)
    sex: str = Field(example="M")
    chessPainType: str = Field(example="ATA")
    restingBP: int = Field(example=140)
    cholesterol: int = Field(example=289)
    fastingBS: str = Field(example=0)
    restingECG: str = Field(example="Normal")
    maxHR: str = Field(example=123)
    exerciseAngina: str = Field(example="N")
    oldpeak: str = Field(example=1.5)
    sTSlope: str = Field(example="Flat")

#root endpoint
@app.get("/")
def root():
    return {"message": "[Rimac Challenge MLE] HeartDisease - LightGBMClassifier"}

#classifier endpoint
@app.post("/classifier")
def predict_heart_disease(item:Item):

    if(not(item)):
        raise HTTPException(status_code=400, 
                            detail = "Error in request, try again...")

    row = []
    row.append({'Age':item.age,
            'Sex':item.sex,
            'ChestPainType':item.chessPainType,
            'RestingBP':item.restingBP,
            'Cholesterol':item.cholesterol,
            'FastingBS':item.fastingBS,
            'RestingECG':item.restingECG,
            'MaxHR':item.maxHR,
            'ExerciseAngina':item.exerciseAngina,
            'Oldpeak':item.oldpeak,
            'ST_Slope':item.sTSlope
    })
    probability = lgbm_clf.predict_proba(pd.DataFrame.from_dict(row, orient='columns'))[0][1]
    return {"prob": float(f'{probability:4f}')}
           

    
