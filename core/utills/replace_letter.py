

letter= {
    'ə': 'e',
    'ç': 'c',
    'ə': 'e',
    'ğ': 'g',
    'ı': 'i',
    'i': 'i',
    'ö': 'o',
    'ş': 's',
    'ü': 'u',
    'Ç': 'C',
    'Ə': 'E',
    'Ğ': 'G',
    'İ': 'I',
    'Ö': 'O',
    'Ş': 'S',
    'Ü': 'U',
    '?' : '',
    ' ' : '-',
    '!' : '',
    '.' : '',
    ',' : '',
    ';' : '',
    ':' : '',
    '*' : '',
    '&' : '',
    '%' : '',
    '^' : '',
    '$' : '',
    '#' : '',
    '@' : '',
}

def replace_letter(text):
  for key, value in letter.items():
    text = text.replace(key, value)
  return text

replace_letter("Bu bir örnek metindir.")
