from djchoices import ChoiceItem, DjangoChoices


class SI_NO(DjangoChoices):
    SI = ChoiceItem('SI')
    NO = ChoiceItem('NO')
    BLANCO = ChoiceItem('--Seleccione--')