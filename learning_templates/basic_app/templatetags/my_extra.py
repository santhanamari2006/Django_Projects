# {% load my_templates %}

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

# register.filter('cut',cut)

#     return value.replace(arg,'') -> kind of putting this whole thing and wrapping it into this nice little custom filter called out

# register.filter('cut',cut) -> call it cut and  pass in the function itself.
