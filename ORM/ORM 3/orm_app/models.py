from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.username
    # autghor modles
    
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="posts")

    def __str__(self):
        return self.title
    
    
    
    # new  models django documentation
    
class Author1(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.OneToOneField(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


    
# bulk create example
        
    class Fruit(models.Model):
        name = models.CharField(max_length=100, primary_key=True)
        colors = models.TextField(null=True, blank=True)

    Fruit.objects.bulk_create([
         Fruit(name='Apple', colors='Red, Green'),
         Fruit(name='Cucumber', colors='Green'),
    ])