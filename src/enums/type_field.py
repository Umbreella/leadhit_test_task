from enum import Enum


class TypeField(str, Enum):
    email = 'email'
    phone = 'phone'
    text = 'text'
    date = 'date'
