from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()
# app.mount("/static", StaticFiles(directory="templates"), name="static")
# templates = Jinja2Templates(directory="templates")
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


class Book(BaseModel):
    title: str
    id: int
    author: str
    publication_year: int
    isbn: str

books = []

@app.post("/books/")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}

@app.get("/books/")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"message": "Book not found"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    update(book_id, updated_book)

    return {"message": "Book not found"}

def update(self, book_id: int, updated_book: Book ):
    for book in books:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            book.publication_year = updated_book.publication_year
            book.isbn = updated_book.isbn
        return {"message": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}
