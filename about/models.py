from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    context = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

