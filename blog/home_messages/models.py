from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    name_blog = models.TextField('Название')
    data_blog = models.DateTimeField('Дата публикации',auto_now_add =True, null=True)
    data_blog_update = models.DateTimeField ('Дата изменения', auto_now =True, null=True )
    description_blog = models.TextField('Описание', null=True)
    name_blogers = models.TextField('Имя блогера')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name_blog,self.data_blog,self.description_blog, self.name_blogers}"

class Category(models.Model):
    name = models.CharField(max_length = 100,db_index =True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('category', kwargs = {'cat_id':self.pk})