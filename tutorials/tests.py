from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

@pytest.mark.parametrize("x, y", [(1, 0), (0, 1), (33, 0), (1000, 10), (-5, 5)])
def test_xy(x, y):
    assert x > y

# Create your tests here.
'''def test_homepage_access():
    url = reverse('home')
    assert url == "/"

#@pytest.mark.django_db
@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

    assert tutorial.title == "Pytest"

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk'''
