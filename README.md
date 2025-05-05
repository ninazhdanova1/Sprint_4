Реализованные тесты

test_add_new_book_add_two_books — проверяет добавление двух уникальных книг.

test_add_new_book_invalid_names_not_added — проверяет, что книги с некорректными названиями (пустыми или слишком длинными) не добавляются.

test_add_new_book_duplicate — убеждается, что одна и та же книга не добавляется дважды.

test_set_book_genre_valid — проверяет корректную установку жанра добавленной книге.

test_added_book_has_no_genre — убеждается, что жанр книги по умолчанию не установлен.

test_get_books_with_specific_genre — проверяет, что метод возвращает книги с определённым жанром.

test_get_books_for_children_excludes_age_restricted — удостоверяется, что книги с возрастным ограничением не попадают в список детских.

test_add_book_in_favorites — проверяет добавление книги в список избранного.

test_add_book_in_favorites_twice — проверяет, что нельзя дважды добавить одну и ту же книгу в избранное.

test_delete_book_from_favorites — проверяет корректное удаление книги из избранного списка.