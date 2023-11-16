from fastapi import FastAPI
from pydantic import BaseModel

var1 = 32
# Creación de una instancia de FastAPI
app = FastAPI()
app.title = "My application with FastAPI"
app.version = "0.0.1"

# Creación de un modelo representativo
class Item(BaseModel):
    name: str
    description: str = None
    price: float = None

# Creación de endpoints (método GET)
@app.get('/', tags = ['home'])  # endpoint 1
def message():
    return f"Hello world! It is my first App. The current value of var1 is {var1}"

@app.get('/items/{item_id}', tags = ['home'])  # endpoint 2
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Creación de endpoints (método POST0)
@app.post('/items/')
async def create_item(item: Item):
    return item
