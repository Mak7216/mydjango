from django.core.exceptions import ValidationError

def my_validation(value):
    if len(value) == 0:
        raise ValidationError("title не может быть пустым")
