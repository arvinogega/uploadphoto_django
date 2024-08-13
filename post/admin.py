from django.contrib import admin
#import the Post model
from .models import Post

# Register your models here.
admin.site.register(Post)