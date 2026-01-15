from django.db import models

class BlogPost(models.Model):
  def __str__(self):
    return self.title

  title = models.CharField()
  intro = models.TextField()
  body = models.TextField()
  pub_date = models.DateField("Published Date")
