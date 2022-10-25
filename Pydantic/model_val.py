from unicodedata import name
from pydantic import BaseModel, ValidationError, validator

class UserModel(BaseModel):
    name:str
    username:str
    password1:str
    password2:str
    
    @validator('name')
    def name_must_contain_space(cls,v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
    
    @validator('password2')
    def password_match(cls,v,values,**kwargs):
        if 'password1' in values and v!=values['password1']:
            raise ValueError('passwords do not match')
        return v
    
    @validator('username')
    def username_alphanumeric(cls,v):
        assert v.isalnum()
        return v
    
user=UserModel(name="Hamza Ihikki",username="ih2k",password1="hahas",password2="hahas")
print(user.dict())
try:
    UserModel(
        name="IHIKKI",
        username="ih2k",
        password1="garer",
        password2="garert"
    )
except ValidationError as e:
    print(e)