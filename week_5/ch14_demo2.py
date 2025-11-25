# Topic(s): Writing Files
# DEMO
# records of books to write to file
books = [
    {"title": "The Cat in the Hat", "author": "Dr. Seuss",
     "year_published": 1605},
    {"title": "The Cat in the Hat Comes Back", "author": "Dr. Seuss",
     "year_published": 1859},
    {"title": "The Adventures of Tom Sawyer", "author": "Mark Twain",
     "year_published": 1876},
    {"title": "The Prince and the Pauper", "author": "Mark Twain",
     "year_published": 1881},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
     "year_published": 1960},
    {"title": "Animal Farm", "author": "George Orwell",
     "year_published": 1945},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger",
     "year_published": 1951},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
     "year_published": 1813}
]

file_path = 'my_books.txt'
# create a file
f = open(file_path, 'w')  # "w" means write (overwrite) mode, 'a' means append to existing file

# extract book info
for book in books:
    # book is a dict
    # book_info = book['title'] + ',' + book['author'] + ',' + str(book['year_published'])
    book_info = ','.join([book['title'], book['author'], str(book['year_published'])])

    # write book info as line on the file
    # print(book_info)  # print() always print on a new line

    f.write(book_info)
    f.write('\n')     # add a new line to start on the next line, like a typewriter

f.close()  # to save and close the file