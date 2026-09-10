import re

from django.core.exceptions import ValidationError


def validate_keyword(name):
    if not name.isalpha():
        raise ValidationError('Ключевое слово {} содержит символы'.format(name))


def validate_username(name):
    """Validate Instagram username syntax locally.

    The original project called Instagram's old ``?__a=1`` endpoint while
    validating a form. That endpoint is no longer a reliable public API and
    can trigger 401/rate-limit responses. This validator intentionally performs
    no network requests. Account existence/access should be checked only by an
    authorized integration layer.
    """
    result = re.fullmatch(r'[A-Za-z0-9._]+', name or '')
    if not result:
        raise ValidationError('Имя пользователя {} содержит запрещенные символы'.format(name))
