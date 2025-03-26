from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_store = {"first_name": "Jane", "last_name": "Doe"}

class Item(BaseModel):
    first_name: str
    last_name: str


@app.get("/")
def sample():
    return {"message": "Data created", "data": data_store}

@app.get("/get_items")
def get_items():
    return data_store  

@app.post("/get_items")
def post_items(item: Item):
    global data_store
    data_store = item.dict()  
    return {"message": "Data created", "data": data_store}

@app.put("/")
def put_items(item: Item):
    global data_store
    data_store = item.dict()  
    return {"message": "Data updated", "data": data_store}

@app.patch("/")
def patch_items(item: Item):
    global data_store
    data_store.update(item.dict(exclude_unset=True))  
    return {"message": "Data patched", "data": data_store}

@app.delete("/")
def delete_items():
    global data_store
    data_store.clear() 
    return {"message": "Data deleted"}
