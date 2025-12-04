from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer ,HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

Security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(Security)) -> dict:
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"DEBUG: Payload decoded successfully: {payload}")

        exp = payload.get("exp")
        if exp and datetime.now(tz=timezone.utc).timestamp() > exp:
            print("DEBUG: Token expired (manual check)")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail= "TOKEN EXPIRADO"
            )
        
        return payload
    
    except jwt.ExpiredSignatureError:
        print("DEBUG: Token expired (jwt library check)")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado"
        )
    except jwt.JWTError as e:
        print(f"DEBUG: JWT Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )
    

def require_role(allowed_roles: list):
    """
    @require_role([3])  # Solo Admin
    @require_role([2, 3])  # Supervisor o Admin
    """
    def role_checker(current_user: dict = Depends(verify_token)) -> dict:
        user_role = current_user.get("role_id")
        
        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"No tienes permisos. Se requiere rol: {allowed_roles}"
            )
        
        return current_user
    
    return role_checker

