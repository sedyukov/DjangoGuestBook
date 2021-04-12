from django.contrib import admin
from .models import ReviewOld
from .models import Review
from .models import Category
# Register your models here.

admin.site.register(Category)
admin.site.register(ReviewOld)
admin.site.register(Review)

