from django.db import models

# Create your models here.

class Blog(models.Model):
    name_blog = models.TextField('Название')
    data_blog = models.DateTimeField('Дата публикации')
    description_blog = models.TextField('Описание', null=True)
    name_blogers = models.TextField('Имя блогера')

    def __str__(self):
        return f"{self.name_blog,self.data_blog,self.description_blog, self.name_blogers}"


