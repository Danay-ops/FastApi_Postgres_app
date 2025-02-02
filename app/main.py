from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import engine, get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.crud.user import get_user, get_users, create_user, update_user, delete_user

User.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=UserInDB)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/", response_model=list[UserInDB])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserInDB)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=UserInDB)
def update_user_info(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=UserInDB)
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
