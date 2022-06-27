from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



# Create your models here.

class categ(models.Model):
    name =models.CharField(max_length=250,unique=True)
    slug =models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)       # for return value -->here we return the name


class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug =models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE) #  on_delete....  is permission annu ,ellagil django error kanikkum


    def get_urls(self):
        return reverse('details',args=[self.category.slug,self.slug])   #passing arrguments (two arguments)      #ethannu home.html le call '{{i.get_urls}}'


    def __str__(self):
        return '{}'.format(self.name)      #this  is for return values in web site it show just 'productname' or somethings to do this methode it will show the  exact name of this ...
