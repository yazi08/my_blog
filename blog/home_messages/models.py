from django.db import models

# Create your models here.

class Blog(models.Model):
    name_blog = models.TextField()
    data_blog = models.TextField()
    description_blog = models.TextField(null=True)
    name_blogers = models.TextField()

    def __str__(self):
        return f"{self.name_blog,self.data_blog,self.description_blog, self.name_blogers}"


