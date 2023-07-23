from django import forms, template

register = template.Library() # если мы не зарегистрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

'''
@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
'''

@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

STOP_LIST=[
    "mat1",
    "mat2",
    "mat3",
]
@register.filter(name='nomat')
def nomat(value, STOP_LIST):
    for world in STOP_LIST:
        if world in value:
            return str("***")