from models.user import User as UserModel
from schemas.user import User


class UserService:
    def __init__(self, DB) -> None:
        self.DB = DB
        
    
    def get_users(self):
        result = self.DB.query(UserModel).all()
        return result
    
    
    def get_user_by_id(self, id: int):
        result = self.DB.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    
    def create_user(self, user: User):
        new_user = UserModel(**user.dict())
        self.DB.add(new_user)
        self.DB.commit()
        return
    
    
    def update_user(self, id: int, user: User):
        result = self.DB.query(UserModel).filter(UserModel.id == id).first()
        
        for key, value in user.dict().items():
            setattr(result, key, value)
        
        self.DB.commit()
        return
    
    
    def delete_user(self, id: int):
        self.DB.query(UserModel).filter(UserModel.id == id).delete()
        self.DB.commit()
        return