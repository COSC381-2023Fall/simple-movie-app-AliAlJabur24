from typing import Union
from movies import Movies
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

movies = Movies(r'C:\Users\Ali Al-Jabur\Desktop\OpenSea Chatbox\simple-movie-app-AliAlJabur24\backend\movies.txt')

app = FastAPI()

## Had to setup middleware for react request to go through
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movie(BaseModel):
    movie_id: int = None
    movie_name: str = None
    Cast: list = None

class Add_Movie(BaseModel):
    movie_id: int = None
    movie_name: str = None
    Cast: list = None

@app.get("/movies/{movie_id}")
async def read_movie(movie_id: int):
    return movies.get_movie_id(movie_id)

@app.put("/movies/{movie_id}")
async def update_Movie(movie_id: int, update_Movie: Movie):
    if movie_id not in range(1, len(movies._movies) + 1):
        raise HTTPException(status_code=404, detail="Movie not found")
    
    movies.update_movie(movie_id, update_Movie.dict(exclude_unset=True))
    
    return movies.get_movie_id(movie_id)

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    movieInfo = movies.get_movie_id(movie_id)
    movies.remove_movie(movie_id)
    return movieInfo

@app.post("/movies/{movie_id}")
async def add_movie(update_Movie: Add_Movie):
    return movies.add_movie(update_Movie.dict(exclude_unset=True))