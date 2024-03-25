import uvicorn
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return{"message": "Hello World"}

@app.post("/")
def predict():
    return{"prediction": "249.0"}


if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=8001,reload=True)
