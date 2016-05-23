from django.contrib import admin
from models import M_Book,M_News,M_Paper,M_Human
from django_summernote.admin import SummernoteModelAdmin,SummernoteWidget,SummernoteInplaceWidget
from django.forms import ModelForm, TextInput

class Book_Form(ModelForm):
    class Meta:
        widgets = {
            'main_body': SummernoteWidget(),
        }

# Register your models here.
@admin.register(M_Book)
class Book_Admin(admin.ModelAdmin):
    form = Book_Form
    list_display = ('title','pub_date')
    search_fields = ('title','main_body')

@admin.register(M_News)
class News_Admin(admin.ModelAdmin):
    form = Book_Form
    list_display = ('title','pub_date')
    search_fields = ('title','main_body')

@admin.register(M_Paper)
class Paper_Admin(admin.ModelAdmin):
    list_display = ('upload','paper_pub_date')

@admin.register(M_Human)
class Human_Admin(admin.ModelAdmin):
    form = Book_Form
    list_display = ('title','pub_date')
    search_fields = ('title','main_body')