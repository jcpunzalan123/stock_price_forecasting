from fastapi import FastAPI 
import uvicorn

app = FastAPI()



@app.get("/ping")
def pong():
    return {"ping": "pong!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")