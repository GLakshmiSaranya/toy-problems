import os, csv
from dbtable import *

def main():
    csvfile = open("books.csv")
    reader = csv.reader(csvfile)
    for isbn, title, author, year in reader:
        book = Book(isbn = isbn, title = title, author = author, year = year)
        db.session.add(book)
    print("Add data")
    db.session.commit()
    print("Add commit")

if __name__ == "__main__":
    with app.app_context():
        main()