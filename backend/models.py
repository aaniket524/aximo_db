from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.

class WorkProcessModel(models.Model):
    title = models.CharField(max_length=100,) 
    desc = models.CharField(max_length=300)
    # FileField(upload_to='svgs/')
    inactiveIcon= models.FileField(upload_to='images/', default='media/images') 
    activeIcon = models.FileField(upload_to='images/',  default='media/images') 

    def __str__(self):
        return self.title

class HomeTestimonialModel(models.Model):
    title = models.CharField(max_length=200)
    desc = RichTextField()
    image = models.ImageField(upload_to='images/')
    user = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class TeamModel(models.Model):
    users = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    prof = models.CharField(max_length=50)
    fburl = models.URLField(max_length=300)
    instaurl =models.URLField(max_length=300)
    twitterurl = models.URLField(max_length=300)
    linkdinurl = models.URLField(max_length=300)

    def __str__(self):
        return self.users



class Services(models.Model):
    title = models.CharField(max_length=100)
    shortdesc = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    thumbimg = models.FileField(upload_to='services/thumbs/', blank=True, null=True)
    redirecticon = models.FileField(upload_to='services/icons/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SingleService(models.Model):
    service = models.OneToOneField(Services, on_delete=models.CASCADE, related_name='detail')
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    featuredimg = models.ImageField(upload_to='singleservice/featured/', blank=True, null=True)
    moreimg = models.ImageField(upload_to='singleservice/more/', blank=True, null=True)
    fulldesc = RichTextField(blank=True, null=True)
    featureone = RichTextField(blank=True, null=True)
    featuretwo = RichTextField(blank=True, null=True)
    process = RichTextField(blank=True, null=True)
    pricing = RichTextField(blank=True, null=True)
    processicon1 = models.FileField(upload_to='singleservice/process/', blank=True, null=True)
    processicon2 = models.FileField(upload_to='singleservice/process/', blank=True, null=True)
    processicon3 = models.FileField(upload_to='singleservice/process/', blank=True, null=True)
    moretext = RichTextField(blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.service.title)
        super(SingleService, self).save(*args, **kwargs)

    def __str__(self):
        return self.service.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True,max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=200)
    thumbnail = models.ImageField(upload_to='blogs/thumbnails/')
    excerpt = models.TextField(blank=True)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title