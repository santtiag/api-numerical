from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import utils
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin

auth_router = APIRouter()

@auth_router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash_password(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

@auth_router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not utils.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = utils.create_access_token(data={"sub": user.email})
    return {"message": "Login successful", "token": access_token}
