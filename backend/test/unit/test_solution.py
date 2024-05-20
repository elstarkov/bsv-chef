import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.controllers.recipecontroller import RecipeController
from src.static.diets import from_string

@pytest.fixture
def sut():
    items_dao= mock.MagicMock()

    return RecipeController(items_dao=items_dao)

@pytest.mark.unit
def test_optimal_normal(sut):
    with mock.patch.object(sut, 'get_readiness_of_recipes', return_value ={'normal': 0.11}):
        res = sut.get_recipe(from_string("normal"), True)
        assert res == 'normal'

@pytest.mark.unit
def test_not_optimal_random_return(sut):
    with mock.patch.object(sut, 'get_readiness_of_recipes', return_value={'normal': 0.1, 'normal2': 0.12}):
        res = sut.get_recipe(from_string("normal"), False)
        assert res in ["normal", "normal2"]

@pytest.mark.unit
def test_low_readiness_value(sut):
    with mock.patch.object(sut, 'get_readiness_of_recipes', return_value={'normal': 0.01}):
        res = sut.get_recipe(from_string("normal"), False)
        assert res == None

@pytest.mark.unit
def test_no_available_recipe(sut):
    with mock.patch.object(sut, 'get_readiness_of_recipes', return_value ={}):
        res = sut.get_recipe(from_string("normal"), True)
        assert res == None
