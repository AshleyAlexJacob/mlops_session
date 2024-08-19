from fastapi import FastAPI
import uvicorn
import mlflow
from models import ModelInput
import pandas as pd
from fastapi.responses import JSONResponse
import pickle

app = FastAPI()

run_id = "2d196898faf74470a5b46035e0a9f6ed"
uri = f"runs:/{run_id}/pipeline_random_forest"

def load_model():
    # return mlflow.sklearn.load_model(uri)
    with open("mlruns/601362966769247400/2d196898faf74470a5b46035e0a9f6ed/artifacts/pipeline_random_forest/model.pkl", 'rb') as file:
        model = pickle.load(file)
        return model

@app.post('/predict')    
def run_predict(data: ModelInput):
    model = load_model()
    data_dict =  data.model_dump()
    model_input = pd.DataFrame([data_dict])
    prediction = model.predict(model_input)[0]
    return JSONResponse({"result": prediction}, status_code=200)
if __name__ == "__main__":
    uvicorn.run("predict:app", host="0.0.0.0", port= 8000)