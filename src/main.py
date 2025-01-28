from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.model_handler import load_models, predict

app = FastAPI(title="Credit Score Prediction API", version="1.0")


# Input schema
class InputData(BaseModel):
    transaction_id: str
    customer_id: str
    account_id: str
    amount: float
    product_category: str
    channel_id: str
    transaction_hour: int
    transaction_day: int
    transaction_month: int
    transaction_year: int


# Load models on startup
@app.on_event("startup")
def startup_event():
    app.state.models = load_models()


@app.get("/")
def root():
    return {"message": "Credit Score Prediction API is running"}


@app.post("/predict/")
def predict_credit_score(data: InputData):
    try:
        model_inputs = data.dict()
        prediction = predict(model_inputs, app.state.models)
        return {"credit_score_prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")
