import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'A' * 41])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Оно')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Интерстеллар')
        collector.set_book_genre('Интерстеллар', 'Фантастика')
        assert collector.get_book_genre('Интерстеллар') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Интерстеллар')
        collector.set_book_genre('Интерстеллар', 'Фантастика')
        collector.add_new_book('Паранормальное')
        collector.set_book_genre('Паранормальное', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Интерстеллар']

    def test_get_books_for_children_excludes_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и Медведь')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()
        assert 'Маша и Медведь' in collector.get_books_for_children()

    def test_add_book_in_favorites_once(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert collector.get_list_of_favorites_books() == []

    def test_get_book_genre_returns_none_if_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_get_books_genre_returns_correct_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        assert collector.get_books_genre() == {'Матрица': 'Фантастика'}
