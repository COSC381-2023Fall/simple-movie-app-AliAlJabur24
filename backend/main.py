from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/movies/{movie_id}")
async def read_movie(movie_id: int):
    return {"movie_id": movie_id, "movie_data": "Fake movie data for example"}