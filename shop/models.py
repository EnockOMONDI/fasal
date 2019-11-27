from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField, FileField
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill 


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Student(models.Model):
    category = models.ForeignKey(Category, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    brief_story = models.TextField(blank=True)
    perfomance_card = FileField()
    document = FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageField(blank=True, null=True, manual_crop="4:4",)
   
     
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
class Media(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = ImageField(blank=True, null=True, manual_crop="4:4",)
      
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:media_detail', args=[self.id, self.slug])

class Team(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    position = models.CharField(max_length=255, db_index=True)
    brief_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = ImageField(blank=True, null=True, manual_crop="4:4",)
      
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:team_detail', args=[self.id, self.slug])
