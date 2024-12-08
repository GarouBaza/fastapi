from fastapi import FastAPI, HTTPException
import unicorn
from pydantic import BaseModel


app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Гарри потер',
        'author': 'Кто то там'
    },
    {
        'id': 2,
        'title': 'Бизнес Идея',
        'author': 'Я'

    }
]

@app.get(
    '/books',
    tags=['Книги'],
    summary='Получить все книги')
def read_books():
    return books

@app.get('/books/{id}', tags=['Книги'], summary='Получить конкретную книгу')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Книга не найдена')

class New_book(BaseModel):
    title: str
    author: str

@app.post('/books')
def create_book(new_book: New_book):
    books.append(
        {   'id': len(books)+1,
            'title': new_book.title,
            'author': new_book.author
        }
    )
    return {'success': True, 'message': 'Yes'}


if __name__ == '__main__':
    unicorn.run('main:app')