from django.db import models
from django.utils import timezone

SIZE = (
  ('XS', 'Extra Small'),
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large'),
  ('XL', 'Extra Large'),
  ('XXL', 'Extra Extra Large'),
  ('XXXL', 'Extra Extra Extra Large'),
)


class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)

  class Meta:
    abstract = True


class Category(BaseModel):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = ("Category")
    verbose_name_plural = ("Category")


class Currency(models.Model):
    code = models.CharField(max_length=6, unique=True)  
    name = models.CharField(max_length=100)             
    symbol = models.CharField(max_length=10)   
         
    def __str__(self):
        return self.code  
    
    class Meta:
      verbose_name = ("Currency")
      verbose_name_plural = ("Currency")


class Color(BaseModel):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = ("Color")
    verbose_name_plural = ("Color")

  def __str__(self):
    return self.name
  

class Size(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
      verbose_name = ("Size")
      verbose_name_plural = ("Size")

    def __str__(self):
        return self.name


class Product(BaseModel):
  name = models.CharField(max_length=50)
  price = models.FloatField()
  color = models.ManyToManyField(Color)
  # size = models.CharField(max_length=50, choices=SIZE, default='M')
  size = models.ManyToManyField(Size)
  like = models.IntegerField(default=0)
  currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name 

  class Meta:
    verbose_name = ("Product")
    verbose_name_plural = ("Product")

  def name_and_price(self):
    return f'{self.name} - {self.price} AZN'
  
  def get_created_year_month_day(self):
    return f'{self.created_at.year} - {self.created_at.month} - {self.created_at.day}'

  def get_discount_price(self):
    return self.price - (self.price * 0.1)


class Blog(BaseModel):
  title = models.CharField(max_length=100)
  desription = models.TextField()
  image = models.ImageField(upload_to='blog/')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = ("Blog")
    verbose_name_plural = ("Blog")

  def format_created_at(self):
    return self.created_at.strftime('%d-%B-%Y')
  

class ContactUs(BaseModel):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = ("Contact Us")
    verbose_name_plural = ("Contact Us")
