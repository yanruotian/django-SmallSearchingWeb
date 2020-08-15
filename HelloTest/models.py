from django.db import models
from django.shortcuts import redirect

# Create your models here.

class Test(models.Model):

    def get(self,request):
        print(request.get('echo_string'))
        return redirect("/test/echo")
