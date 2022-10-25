# Quick start with Flask and FastAPI
 This repository focuses on the different technologies and tools, which will serve as a starting point to move from a research environment to a production environment.

## We will discover how to deploy a machine learning model in local mode
- open the 'Furniture prediction notebook', and run it to produce the file 'model.pkl'.
- we will work with the furniture database: 'furniture.csv'.

## Pytest
The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

pytest requires: Python 3.7+ or PyPy3.
```python
#my_module.py
def square(x):
    return x ** 2

```
```python
#test_my_module.py
from my_module import square
def test_square_gives_correct_value():
    subject= square(2)
    assert subject == 4

```
## Pydantic
Pydantic is a library for data validation and parameter management using python type annotations. It enforces type conversions at runtime and provides user-friendly errors when data is not valid.
```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] =None
    friends: List[int] = []
    external_data = { 'id': '123', 'signup_ts': '2019-06-01 12:22', 'friends': [1, 2, '5'], }
user = User(**external_data)
print(user.id) #> 123
print(repr(user.signup_ts)) #> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends) #> [1, 2, 3] print(user.dict())

```
## FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.

```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```
~~~shell
$ uvicorn main:app --reload
~~~~
> - main: est le fichier main dans le module python
> - app : est l’objet crée dans main.py (i.e., la ligne app = FastAPI())
o
> - --reload : pour redémarrer le serveur après chaque changement du code (seulement dans un environnement de développement)
