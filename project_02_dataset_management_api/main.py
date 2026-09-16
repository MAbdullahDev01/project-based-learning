# Create an api to store, view and delete data stored about datasets in sqlite3 db
from fastapi import FastAPI
from routers import health
from routers import create_dataset

app = FastAPI()

@app.get("/")
def root():
    return("Hello: World")

app.include_router(create_dataset.router)
app.include_router(health.router)