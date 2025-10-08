from django.db.models import Count
from ..models import Author,Books


def run():
    # author = Author.objects.create(name = 'Tohir Malik',birthday = 1958)
    # author2 = Author.objects.create(name='Erkin A’zam', birthday=1950)
    # author3 = Author.objects.create(name='O‘tkir Hoshimov', birthday=1941)
    
    # Books.objects.create(name = 'Shaytanat',year = 1993,author_id = 1)
    #  Books.objects.create(name = "So'ngi o'q",year = 1998,author_id = 1)
    #  Books.objects.create(name='Odamiylik mulki', year=2005, author_id=1)
    
    # Books.objects.create(name='Dunyoning ishlari', year=1995, author_id=3)
    # Books.objects.create(name='Jannat ostonasida', year=2001, author_id=3)
    # Books.objects.create(name='Bahor qaytmaydi', year=1992, author_id=3)

    # Books.objects.create(name='Urushning so‘nggi qurboni', year=1980, author_id=4)
    # Books.objects.create(name='Tushda kechgan umrlar', year=1983, author_id=4)
    # Books.objects.create(name='Ikki eshik orasi', year=1986, author_id=4)

    # authors = Author.objects.all()
    # for author in authors:
    #   print(author.name)

    # books = Books.objects.filter(year__gt = 1950)
    # for book in books:
    #   print(book.name,book.year)

    # author = Author.objects.get(name = "Tohir Malik")
    # books = Books.objects.filter(author = author)
    # for book in books:
    #     print(book.name,book.author)

    # authors = Author.objects.annotate(book_count = Count('books'))
    # for author in authors:
    #     print(author.name,author.book_count)
    
    # book = Books.objects.get(name = 'Shaytanat')
    # book.name = "Shaytanat (To'liq nashir)"
    # book.save()
    # print(book)

    # author = Author.objects.get(name = "Erkin A’zam")
    # author.name = "Erkin A'zam"
    # author.birthday = 1951
    # author.save ()
    # print(author)

    # book = Books.objects.get(name = "Bahor qaytmaydi").delete()
    # print("O'chirildi")

    # author = Author.objects.get(name = "Erkin A'zam").delete()
    # print("Ochirildi")



