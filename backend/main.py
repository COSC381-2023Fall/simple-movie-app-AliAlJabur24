from typing import Union
from movies import Movies
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

movies = Movies(r'C:\Users\Ali Al-Jabur\Desktop\OpenSea Chatbox\simple-movie-app-AliAlJabur24\backend\movies.txt')

app = FastAPI()

class Movie(BaseModel):
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
