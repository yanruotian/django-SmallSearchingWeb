from django.db import models

# Create your models here.

class Articles(models.Model):
    content = models.TextField(max_length=1000)

    def __str__(self):
        if len(self.content) <= 10:
            return self.content
        else:
            return self.content[:8]+'……'

    def show(self, num:int):
        if len(self.content) <= num:
            return self.content
        else:
            return self.content[:num - 2]+"……"
