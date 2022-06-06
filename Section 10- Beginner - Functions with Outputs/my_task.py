# Functions with outputs

from turtle import title


def format_name(f_name, l_name):
    """ selamın aleykum
    kardeesss
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'{formated_f_name} {formated_l_name}'


print(format_name('caglayan', 'caliskan'))
