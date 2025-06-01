from fastapi import FastAPI, HTTPException, status, Depends
from . import models
from app import schemas
from typing import List
from app.db import get_db, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()



def validate_book(book):
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')



@app.get('/books', response_model=List[schemas.Book])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Book).all()
    return posts


@app.post('/books', response_model=schemas.Book)
def create_posts(book: schemas.BookCreate, db: Session = Depends(get_db)):
    books_dict = book.model_dump()
    new_book = models.Book(**books_dict)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get('/books/{id}',  response_model=schemas.Book)
def get_post(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    validate_book(book)
    return book


@app.delete('/books/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()
    book_title = book.title
    validate_book(book)
    book_query.delete(synchronize_session=False)
    db.commit()

    return {"deleted": f"Book with id {id} and title '{book_title}' was deleted."}

@app.put('/books/{id}', response_model=schemas.Book)
def update_post(book: schemas.BookCreate, id: int, db: Session = Depends(get_db)):
    update_book_query = db.query(models.Book).filter(models.Book.id == id)
    update_post = update_book_query.first()
    validate_book(update_post)
    
    update_book_query.update(book.model_dump())
    db.commit()
    
    db.refresh(update_post)
    return update_post


