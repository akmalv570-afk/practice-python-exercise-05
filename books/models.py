from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name}-{self.birthday}"


class Books(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return f"[Book:{self.name}\nYear:{self.year}\nAuthor:{self.author}]"