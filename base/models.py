from django.db import models
from ckeditor.fields import RichTextField

TYPE = {("row","row"),
        ("colon","colon"),}

    
class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="picturs")    
    def __str__(self):
        return str(self.image)



class Projects(models.Model):
    title = models.CharField(max_length=50)
    storyline =models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="picturs")
    body = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self) :
        return self.title  


class Comment(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    number = models.CharField(max_length=20,null=True)

  
    def __str__(self):
        return self.name    
 
class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name        