from django.db import models

# Create your models here.
class Topics(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    topic_name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.CharField(max_length=100,default='india@gmail.com')

    def __str__(self):
        return self.name
    


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author

