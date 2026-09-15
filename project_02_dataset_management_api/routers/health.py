from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health():
    print("Health: Good!")
    return {"status": "Good"}