from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    head0 = models.CharField(max_length=200, default='')
    chead0 = models.TextField(default='')
    head1 = models.CharField(max_length=200, default='')
    chead1 = models.TextField(default='')
    head2 = models.CharField(max_length=200, default='')
    chead2 = models.TextField(default='')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to = 'blog/images', default='')
    
    def __str__(self):
        return self.title 