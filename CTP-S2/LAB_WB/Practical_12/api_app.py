from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Item Management API", version="1.0")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items_db: List[Item] = []

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be non-negative.")
    items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_app:app", host="127.0.0.1", port=8000, reload=True)
