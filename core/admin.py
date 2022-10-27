from django.contrib import admin
from .models import Favorite, User, Resource, Category

admin.site.register(User)
admin.site.register(Resource)
admin.site.register(Favorite)
admin.site.register(Category)
