from django import template

register = template.Library()

@register.filter(name='NoMat')

STOP_LIST = [
    'мат',
    'мат',
    'мат',
]

    def NoMat(value, STOP_LIST):
        value = self.cleaned_data['value']
        for word in STOP_LIST:
            if word in value:
                raise forms.ValidationError("Вы позволили себе немного лишнего! Одумайтесь и исправьте текст!")
        return value