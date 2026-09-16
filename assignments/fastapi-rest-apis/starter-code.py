from fastapi import FastAPI

app = FastAPI(title="Task API")

items = [
    {"id": 1, "name": "Write code", "done": False},
    {"id": 2, "name": "Study Python", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}


@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
