from datetime import datetime
from typing import List,Optional
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name="IHIKKI Hamza"
    signup_ts:Optional[datetime]=None
    friends:List[int]=[]
    
external_data={
    'id':'12a3',
    'signup_ts':'2022-10-11 20:21',
    'friends':[1,2,'5']
}
user=User(**external_data)
print(user.id,type(user.id))
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
