from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)



def test_create_book():
    response = client.post("/books", json={
        "title": "Test Book",
        "author": "Author",
        "year": 2020,
        "genre": "Fiction"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Author"
    assert data["year"] == 2020
    assert data["genre"] == "Fiction"
    assert "id" in data

def test_get_books_empty():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []

def test_get_books():
   
    client.post("/books", json={
        "title": "Book",
        "author": "Author",
        "year": 2019,
    })
    client.post("/books", json={
        "title": "Book2",
        "author": "Author2",
        "year": 2021,
    })

    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Book"
    assert data[1]["title"] == "Book2"

def test_get_single_book():
    create_response = client.post("/books", json={
        "title": "Single Book",
        "author": "Author",
        "year": 2018,
    })
    book_id = create_response.json()["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Single Book"
    assert data["author"] == "Author"

def test_get_single_book_not_found():
    response = client.get("/books/9999")
    assert response.status_code == 404


def test_update_book_not_found():
    response = client.put("/books/9999", json={
        "title": "Doesn't Exist",
        "author": "No One",
        "year": 2000,
    })
    assert response.status_code == 404


def test_delete_book_not_found():
    response = client.delete("/books/9999")
    assert response.status_code == 404