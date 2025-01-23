# База данных книг
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# Класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):

        self.id = id  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц

    def __str__(self) -> str:

        return f'Книга "{self.name}"'

    def __repr__(self) -> str:

        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# Основная программа
if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)