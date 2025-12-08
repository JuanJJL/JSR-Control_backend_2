from fastapi import APIRouter, HTTPException
from ..database.Auth_schema import Token_response, Login_request
from ..controllers.AuthController import check_credentials, create_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(credentials: Login_request):
    print(credentials)
    user = await check_credentials(
        credentials.username,
        credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )
    
    token = create_token(user)

    return {
        "access_token": token,
        "token_type": "bearer",
        "role_id": user.role_id
    }
    #1



