from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Shiv'}}


@app.get('/blog')
def index(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return {'data': f"{limit} published blogs from db"}
    else:
        return {'data': f"{limit} blogs from db"}

@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/unpublished')
def show():
    return {'data': 'showing unpublished blogs'}


@app.get('/blog/{id}')
def show(id):
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id, limit=10):
    return {'data': {'a', 'b'}}


@app.get('/blog2/{id}')
def show(id: int):
    return {'data': id}

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data': f"Blog is created with title as {request.title}"}