from datetime import datetime
from typing import Optional
import uuid
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI()

def generate_new_id():
    return uuid.uuid4()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    post_id: uuid.UUID = Field(default_factory=generate_new_id)
    rating: Optional[int] = None

class Comment(BaseModel):
    post_id: uuid.UUID
    comment_id: uuid.UUID = Field(default_factory=generate_new_id)
    content: str
    created_at: datetime = Field(default_factory=datetime.now)

posts = {
    str(uuid.uuid4()): Post(title="My first post", content="This is the first post", published=True, rating=5)
    for _ in range(10)
}

comments = {
    str(uuid.uuid4()): Comment(post_id=list(posts.keys())[0], content=f"This is comment {i}")
    for i in range(1, 8)
}

def get_post(post_id: uuid.UUID) -> Optional[Post]:
    return posts.get(str(post_id))

@app.get("/posts")
def read_posts():
    return posts

@app.get("/posts/{post_id}")
def read_post(post_id: uuid.UUID):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail=f"Post id {post_id} not found")
    return post

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_id_str = str(post.post_id)
    posts[post_id_str] = post
    return {"message": "Post created successfully", "data": post}

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: uuid.UUID):
    post_id_str = str(post_id)
    if post_id_str not in posts:
        raise HTTPException(status_code=404, detail=f"Post id {post_id} not found")
    del posts[post_id_str]
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{post_id}")
def update_post(post_id: uuid.UUID, updated_post: Post):
    post_id_str = str(post_id)
    if post_id_str not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id {post_id} not found")
    posts[post_id_str] = updated_post
    return {"message": "Update successful", "data": updated_post}

@app.patch("/posts/{post_id}")
def update_post_partially(post_id: uuid.UUID, updated_fields: dict = Body(...)):
    post_id_str = str(post_id)
    if post_id_str not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id {post_id} not found")
    post = posts[post_id_str]
    for field, value in updated_fields.items():
        setattr(post, field, value)
    return {"message": "Update successful", "data": post}

@app.get("/posts/rating/{post_id}")
def get_post_rating(post_id: uuid.UUID):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id {post_id} not found")
    return {"rating": post.rating}

@app.post("/post/{post_id}/comments", status_code=status.HTTP_201_CREATED)
def create_comment(post_id: uuid.UUID, comment: Comment):
    if str(post_id) not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id {post_id} not found")
    comment.post_id = post_id
    comments[str(comment.comment_id)] = comment
    return {"message": "Comment created successfully", "data": comment}

@app.get("/post/{post_id}/comments")
def get_comments(post_id: uuid.UUID):
    post_id_str = str(post_id)
    if post_id_str not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id {post_id} not found")
    return comments
