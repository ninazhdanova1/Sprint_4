Реализованные тесты

test_add_new_book_add_two_books — проверка, что можно добавить две книги.

test_add_new_book_invalid_name_length — параметризованный тест: книга не добавляется, если название пустое или слишком длинное.

test_add_new_book_duplicate_not_added — дублирующаяся книга не добавляется.

test_set_book_genre_successfully — установка жанра для одной книги.

test_set_book_genre_with_multiple_books — установка жанра для нескольких книг.

test_get_books_with_specific_genre_returns_correct_books — получение книг по определённому жанру.

test_get_books_for_children_excludes_age_restricted_genres — проверка, что книги с возрастными жанрами не попадают в список детских книг.

test_add_book_in_favorites_once — книга не дублируется в избранном при повторном добавлении.

test_get_list_of_favorites_books_returns_correct_list — возвращается корректный список избранных книг.

test_delete_book_from_favorites_removes_book — удаление книги из избранного.

test_get_book_genre_returns_empty_if_not_set — если жанр не задан, возвращается пустая строка.

test_get_books_genre_returns_correct_dictionary — словарь жанров книг формируется правильно.
