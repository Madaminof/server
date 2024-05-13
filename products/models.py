from django.urls import reverse
from django.db import models

# Create your models here.


class BookCategory(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table='book_category'
    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    coment=models.TextField()
    star_given=models.IntegerField()
    class Meta:
        db_table='book_review'
    def __str__(self) -> str:
        return self.coment

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    author_review=models.ForeignKey(Review,on_delete=models.CASCADE)
    class Meta:
        db_table='book_author'
    def __str__(self) -> str:
        return f"{self.first_name}  {self.author_review.coment}  {self.author_review.star_given}"
    




class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(to="BookCategory", on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField()
    page=models.IntegerField()
    price=models.IntegerField()
    image = models.ImageField(upload_to='book/', default='media/default_img/default_book_img.jpg')

    class Meta:
        db_table='books'

    def __str__(self) -> str:
        return f"{self.category.name} {self.name}  {self.author.first_name}  {self.author.author_review.coment}"    

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})



