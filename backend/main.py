from typing import Union
from movies import Movies
from fastapi import FastAPI

movies = Movies(r'backend\movies.txt')

app = FastAPI()


@app.get("/movies/{movie_id}")
async def read_movie(movie_id: int):
    return movies.get_movie_id(movie_id)

