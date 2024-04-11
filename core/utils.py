from django.utils.text import slugify


def slugify_malefashion(s):
  s = s.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u').replace(
    'ş', 's').replace('ç', 'c').replace('ö',
                                        'o').replace('ə',
                                                     'a').replace(' ', '_')
  s = s.lower()
  s = slugify(s, allow_unicode=True)
  return s
