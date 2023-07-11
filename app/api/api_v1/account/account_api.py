from fastapi.routing import APIRouter

router = APIRouter(prefix='/account')

@router.post("/login")
def login():
    return {
        "username": "John Doe",
    }
