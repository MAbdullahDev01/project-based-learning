from fastapi import APIRouter
from pydantic import BaseModel
from sqlite3 import Error

from database import create_dataset

router = APIRouter()

class Dataset(BaseModel):
    name : str
    description : str | None
    created_at : str

@router.post("/new_dataset/")
def new_dataset(dataset : Dataset):
    try:
        create_dataset(dataset.name, dataset.description, dataset.created_at)
    except Error as e:
        return f"Error occurred {e}"

    return "Successfully stored"