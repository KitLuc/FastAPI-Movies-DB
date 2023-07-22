from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import SESSION
from schemas.user import User
from services.user import UserService
from utils.jwt_manager import create_token


user = APIRouter()


@user.post("/login/", tags=['auth'], status_code=200, response_model=list[User])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})


@user.get("/users/", status_code=200, response_model=list[User])
def get_all_users() -> list[User]:
    DB = SESSION()
    users = UserService(DB).get_users()
    return users


@user.get("/users/{user_id}", status_code=200, response_model=User)
def get_user_by_id(user_id: int) -> User:
    DB = SESSION()
    user = UserService(DB).get_user_by_id(user_id)
    return user


@user.post("/users/", status_code=201)
def create_user(user: User):
    DB = SESSION()
    UserService(DB).create_user(user)
    return {"message": "User created"}


@user.put("/users/{id}", status_code=200)
def update_user(id: int, user: User):
    DB = SESSION()
    UserService(DB).update_user(id, user)
    return {"message": "User updated"}


@user.delete("/users/{id}", status_code=200)
def delete_user(id: int):
    DB = SESSION()
    UserService(DB).delete_user(id)
    return {"message": "User deleted"}
