from ast import Bytes
from io import BytesIO
from django.db import models
from django.shortcuts import reverse
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode

# Create your models here.



class Profile(models.Model):
    firstname=models.CharField(max_length=51)
    lastname=models.CharField(max_length=51)
    about=models.TextField(default='yes')
    email=models.EmailField()
    picture=models.FileField(upload_to='profile/')
    qr_code=models.ImageField(upload_to='qr_codes/')
    user_id=models.CharField(max_length=12)
    profession=models.CharField(max_length=24,default='Software Engineer')
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    def get_absolute_url(self):
        return reverse('profile',kwargs={'slug':self.user_id})
    def get_edit_profile_url(self):
        return reverse('edit_profile',kwargs={'slug':self.user_id})
    
    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make('nautilusprofile.herokuapp.com'+self.get_absolute_url())
        canvas=Image.new('RGB',(350, 350),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.firstname}/{self.lastname}/qr_code.png'
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)



class Page(models.Model):
    heading=models.CharField(max_length=45)
    description = models.TextField()
    web_name = models.TextField
    def __str__(self):
        return f"{self.webname}"


class Gallery(models.Model):
    # image=models.TextField()
    # image_name=models.TextField()
    picture=models.FileField(upload_to='profile/')
    user_id=models.CharField(max_length=45)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.image_name}"

    def get_absolute_gallery_url(self):
        return reverse('add_gallery')