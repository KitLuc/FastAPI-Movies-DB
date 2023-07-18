from fastapi import APIRouter
from pydantic import BaseModel
from models.user import User as UserModel
from config.database import SESSION
from schemas.user import User


user = APIRouter()


@user.get("/users/", status_code=200, response_model=list[User])
async def get_all_users() -> list[User]:
    DB = SESSION()
    users = await DB.query(UserModel).all()
    return users


@user.get("/users/{user_id}", status_code=200, response_model=User)
async def get_user_by_id(user_id: int) -> User:
    DB = SESSION()
    user = await DB.query(UserModel).filter(UserModel.id == user_id).first()
    return user


@user.post("/users/", status_code=201)
async def create_user(user: User):
    DB = SESSION()
    new_user = await UserModel(**user.dict())
    DB.add(new_user)
    DB.commit()
    return {"message": "User created"}


@user.put("/users/{user_id}", status_code=200)
async def update_user(user_id: int, user: User):
    DB = SESSION()
    user = await DB.query(UserModel).filter(UserModel.id == user_id).first()

    for key, value in user.dict().items():
        setattr(user, key, value)

    return {"message": "User updated"}


@user.delete("/users/{user_id}", status_code=200)
async def delete_user(user_id: int):
    DB = SESSION()
    user = await DB.query(UserModel).filter(UserModel.id == user_id).first()
    DB.delete(user)
    DB.commit()
    return {"message": "User deleted"}
