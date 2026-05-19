from fastapi import APIRouter

from src.main.services.movies_service import create_movie_service
from src.main.validators import MovieCreateResponse, MovieCreateValidator

movies_router = APIRouter(tags=["Movies"])


@movies_router.post("/movies", response_model=MovieCreateResponse, status_code=201)
async def create_movie_route(body: MovieCreateValidator):
    created_movie = create_movie_service(body)
    return {
        "message": "Movie created successfully",
        "data": created_movie,
    }