from django.db import models
from django.utils import timezone

# Create your models here.
class M_Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    pub_date = models.DateTimeField(verbose_name='Publish Date', auto_now_add=True)
    main_body = models.TextField(max_length=100000, verbose_name='Main Body')

class M_News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    pub_date = models.DateTimeField(verbose_name='Publish Date', auto_now_add=True)
    main_body = models.TextField(max_length=100000, verbose_name='Main Body')

class M_Paper(models.Model):
    upload = models.FileField(upload_to='sflawyer/static/sflawyer/doc')
    paper_pub_date = models.DateField(verbose_name='Paper Publish Date')
    pub_date = models.DateTimeField(verbose_name='Publish Date', auto_now_add=True)

    def GetDocName(self):
        return self.upload.name[29:]

    def GetDocName_S(self):
        return self.upload.name[29:49]

    def GetDocStaticUrl(self):
        return self.upload.name[8:]

    def Getpaper_pub_date_Txt(self):
        return '/'.join([str(self.paper_pub_date.year),str(self.paper_pub_date.month),str(self.paper_pub_date.day)])

class M_Human(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    pub_date = models.DateTimeField(verbose_name='Publish Date', auto_now_add=True)
    main_body = models.TextField(max_length=100000, verbose_name='Main Body')