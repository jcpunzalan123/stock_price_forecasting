from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
import uvicorn
from model import convert, predict

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str

class StockOut(StockIn):
    forecast: dict



# route
@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")