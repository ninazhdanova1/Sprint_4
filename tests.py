import pytest
from main import BooksCollector

# Фикстура создаёт новый экземпляр BooksCollector для каждого теста
@pytest.fixture
def collector():
    return BooksCollector()

# Тест на добавление двух книг
def test_add_new_book_add_two_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    assert len(collector.get_books_genre()) == 2

# Параметризация: проверка некорректных названий
@pytest.mark.parametrize('book_name', ['', 'А' * 41])
def test_add_new_book_invalid_names_not_added(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name not in collector.get_books_genre()

# Тест: повторное добавление одной и той же книги
def test_add_new_book_duplicate(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Дюна')
    assert len(collector.get_books_genre()) == 1

# Тест: установка жанра книге
def test_set_book_genre_valid(collector):
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    assert collector.get_book_genre('1984') == 'Фантастика'

# Тест: у добавленной книги нет жанра по умолчанию
def test_added_book_has_no_genre(collector):
    collector.add_new_book('Без жанра')
    assert collector.get_book_genre('Без жанра') == ''

# Тест: список книг с определённым жанром
def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Шерлок')
    collector.set_book_genre('Шерлок', 'Детективы')
    assert collector.get_books_with_specific_genre('Детективы') == ['Шерлок']

# Тест: книги с возрастным рейтингом отсутствуют в списке детских
def test_get_books_for_children_excludes_age_restricted(collector):
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.add_new_book('Корпорация монстров')
    collector.set_book_genre('Корпорация монстров', 'Мультфильмы')
    result = collector.get_books_for_children()
    assert 'Оно' not in result
    assert 'Корпорация монстров' in result

# Тест: добавление книги в избранное
def test_add_book_in_favorites(collector):
    collector.add_new_book('Хоббит')
    collector.add_book_in_favorites('Хоббит')
    assert collector.get_list_of_favorites_books() == ['Хоббит']

# Тест: книга не добавляется повторно в избранное
def test_add_book_in_favorites_twice(collector):
    collector.add_new_book('Хоббит')
    collector.add_book_in_favorites('Хоббит')
    collector.add_book_in_favorites('Хоббит')
    assert collector.get_list_of_favorites_books() == ['Хоббит']

# Тест: удаление книги из избранного
def test_delete_book_from_favorites(collector):
    collector.add_new_book('Хоббит')
    collector.add_book_in_favorites('Хоббит')
    collector.delete_book_from_favorites('Хоббит')
    assert collector.get_list_of_favorites_books() == []
