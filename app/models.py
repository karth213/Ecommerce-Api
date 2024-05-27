from django.db import models
from django.core.files import File
from PIL import Image
from io import BytesIO

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length = 99)
    slug = models.SlugField()


    class Meta:
        ordering = ('Name',)
    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=models.CASCADE)
    name = models.CharField(max_length = 99)
    slug = models.SlugField()
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    image = models.ImageField(upload_to = 'uploadsi/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to = 'uploadsi/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/' 
    
    def get_image(self):
        if self.image:
            return 'https://127.0.0.0:8000' + self.image.url
        
    def get_thumnail(self):
        if self.thumbnail:
            return 'https://127.0.0.0:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)

            else:
                return ''
            
        def make_thumbnail(self, image, size=(300,200)):
            img = Image.open(image)
            img.convert('RGB')
            img.thumbnail(size)

            thum_io = BytesIO()
            img.save(thum_io, 'JPEG', quality = 78)

            thumbnail = File(thum_io, name = image.name)

            return thumbnail




        


