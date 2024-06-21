from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class User(BaseModel):
    username: str
    hostname: str

# Example data
items_data = [
    {"name": "item1", "price": 10.5, "is_offer": True},
    {"name": "item2", "price": 20.0, "is_offer": False},
]

@app.get("/api/user", response_model=User)
def read_user():
    import socket
    import getpass
    return {
        "username": getpass.getuser(),
        "hostname": socket.gethostname()
    }

@app.get("/api/items/", response_model=List[Item])
def read_items():
    return items_data

@app.get("/api/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id < len(items_data):
        return items_data[item_id]
    else:
        return {"error": "Item not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
