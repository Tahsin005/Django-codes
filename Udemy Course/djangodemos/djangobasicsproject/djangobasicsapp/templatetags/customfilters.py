from django import template
from num2words import num2words


register = template.Library()

def first_five_upper(value):
    result = value[:5].upper()
    return result

def first_n_upper(value, n):
    result = value[:n].upper()
    return result

def length_limit(value, limit):
    if len(value) > limit:
        return value[0:limit] + '...'
    return value

def rating(value):
    if float(value) >= 4:
        return value + '[Excellent]'
    elif float(value) >= 3:
        return value + '[Good]'
    elif float(value) >= 2:
        return value + '[Average]'
    else:
        return value + '[Poor]'

def number_to_words(value):
    return num2words(int(value))


register.filter('firstfiveupper', first_five_upper)
register.filter('firstnupper', first_n_upper)
register.filter('lengthlimit', length_limit)
register.filter('rating', rating)
register.filter('numtowords', number_to_words)