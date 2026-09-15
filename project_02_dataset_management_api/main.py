# Create an api to store, view and delete data stored about datasets in sqlite3 db
from fastapi import FastAPI
from routers import health

app = FastAPI()

@app.get("/")
def root():
    return("Hello: World")

app.include_router(health.router)