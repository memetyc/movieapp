from django.db import models
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.address}'

class Person(models.Model):
    genders =(
        ('M','Male'),
        ('F','Female')
    )
    duty_types=(
        ('1','Crew'),
        ('2','Cast'),
        ('3','Director'),
        ('4','Writer'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.FileField(upload_to='images_person',default='')
    date_of_bith = models.DateField()
    gender = models.CharField('Cinsiyet',max_length=1, choices=genders)
    duty_type = models.CharField('Gorev',max_length=1, choices=duty_types)

    contact = models.OneToOneField(Contact,on_delete=models.CASCADE,null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
  
    full_name.fget.short_description = 'Ad soyad'


    class Meta:
        verbose_name = 'Kisi'
        verbose_name_plural = 'Kisiler'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})'

class Movie(models.Model):
    title = models.CharField('Baslik',max_length=100)
    description = RichTextField()
    image_name = models.FileField(upload_to='images',default="")
    image_cover = models.FileField(upload_to='images',default="")
    date = models.DateField()
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=19,decimal_places=2)
    language = models.CharField(max_length=50)
    is_active = models.BooleanField('Gosterimde',default=False)
    is_home = models.BooleanField('Anasayfada',default=False)
    # slide_img = models.FileField(upload_to='images',default="")
    
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse("movie_details", kwargs={"slug": self.slug})
    

    

#admin panelindeki isim degisimi icin
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmler'

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movies')
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Kapak resmi'
        verbose_name_plural = 'Kapak resimleri'

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Comment(models.Model):

    stars = (
        ('1','1 Star'),
        ('2','2 Star'),
        ('3','3 Star'),
        ('4','4 Star'),
        ('5','5 Star'),
    )

    full_name = models.CharField(max_length=70)
    email = models.EmailField(default='')
    ratting = models.CharField(null=True,max_length=1,choices=stars)
    text = models.TextField(max_length=500)
    tarih = models.DateField(null=True,auto_now=True)

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.full_name
    
