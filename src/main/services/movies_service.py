import sqlite3
from typing import Any, Dict

from fastapi import HTTPException

from src.main.repositories.movies_repository import create_movie_repo
from src.main.validators import MovieCreateValidator


def create_movie_service(body: MovieCreateValidator) -> Dict[str, Any]:
    data = body.model_dump()
    try:
        return create_movie_repo(data)
    except sqlite3.Error as exc:
        raise HTTPException(status_code=500, detail="Error saving movie") from exc
