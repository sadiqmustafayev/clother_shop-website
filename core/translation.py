from atexit import register
from modeltranslation.translator import translator, TranslationOptions
from core.models import Blog, Product, Color


class BlogsTranslationOptions(TranslationOptions):
  fields = (
    'title',
    'desription',
    'aforism',
  )


translator.register(Blog, BlogsTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = (
      'currency',
      'color',
    ) 

translator.register(Product, ProductTranslationOptions)


class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Color, ColorTranslationOptions)