from django.contrib import admin
from .models import Product,ProductAttribute,ProductAttributeValue,ProductImages,ProductReview

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
