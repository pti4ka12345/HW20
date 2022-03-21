from unittest.mock import MagicMock

import pytest

from HW20.demostration_solution.dao.genre import GenreDAO
from HW20.demostration_solution.dao.model.genre import Genre
from HW20.demostration_solution.service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(
        id=1,
        name="Gen1",
    )
    genre2 = Genre(
        id=2,
        name="Gen2",
    )
    genre3 = Genre(
        id=3,
        name="Gen3",
    )
    dict_object = {1: genre1, 2: genre2, 3: genre3}
    genre_dao.get_one = MagicMock(side_effect=dict_object.get)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=4, name="Gen4"))
    genre_dao.delete = MagicMock(side_effect=dict_object.pop)
    genre_dao.update = MagicMock()
    genre_dao.partially_update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "Gen4"
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)
        genre = self.genre_service.get_one(1)
        assert genre is None

    def test_update(self):
        genre_d = {
            "id": 2,
            "name": "Gen2_upd",
                    }
        self.genre_service.update(genre_d)
