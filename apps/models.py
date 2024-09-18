from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from django.utils.text import slugify


# Create your models here.

class BaseCreatedModel(Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseSlugModel(Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        if self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += 1
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Category(BaseSlugModel, BaseCreatedModel):
    pass


class Product(BaseSlugModel, BaseCreatedModel):
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')




