from modeltranslation.translator import translator, TranslationOptions
from core.models import Blog


class BlogsTranslationOptions(TranslationOptions):
  fields = (
    'title',
    'desription',
    'aforism',
  )


translator.register(Blog, BlogsTranslationOptions)

 
