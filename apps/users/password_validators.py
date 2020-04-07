from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class BigAndSmallLetterPasswordValidator:
    def __init__(self, min_cap_letters=1, min_small_letters=1):
        self.min_cap_letters = min_cap_letters
        self.min_small_letters = min_small_letters

    def validate(self, password, user=None):
        cap_letters = len(list(filter(lambda letter: letter.isupper(), [letter for letter in password])))
        small_letters = len(list(filter(lambda letter: letter.islower(), [letter for letter in password])))
        if cap_letters < self.min_cap_letters and small_letters < self.min_small_letters:
            raise ValidationError(
                _("Wymagana ilośc dużych liter: %(min_cap_letters)d oraz małych liter %(min_small_letters)d"),
                code='not_enough_cap_and_small_letters',
                params={'min_cap_letters': self.min_cap_letters,
                        'min_small_letters': self.min_small_letters},
            )
        if cap_letters < self.min_cap_letters:
            raise ValidationError(
                _("Wymagana ilośc dużych liter: %(min_cap_letters)d"),
                code='not_enough_cap_letters',
                params={'min_cap_letters': self.min_cap_letters},
            )
        if small_letters < self.min_small_letters:
            raise ValidationError(
                _("Wymagana ilośc małych liter: %(min_small_letters)d"),
                code='not_enough_small_letters',
                params={'min_small_letters': self.min_small_letters},
            )

    def get_help_text(self):
        return _(
            "Wymagana ilośc dużych liter: %(min_cap_letters)d. Wymagana ilośc małych liter: %(min_small_letters)d."
            % {'min_cap_letters': self.min_cap_letters,
               'min_small_letters': self.min_small_letters}
        )


class ContainsDigitAndSpecialSignPasswordValidator:
    def __init__(self, min_digits=1, min_special_chars=1):
        self.min_digits = min_digits
        self.min_special_chars = min_special_chars

    def validate(self, password, user=None):
        digits = len(list(filter(lambda letter: letter.isnumeric(), [letter for letter in password])))
        special_chars = len(list(filter(lambda letter: not letter.isalnum(), [letter for letter in password])))
        if digits < self.min_digits and special_chars < self.min_special_chars:
            raise ValidationError(
                _("Wymagana ilośc cyfr: %(min_digits)d. Wymagana ilośc znaków specjalnych: %(min_special_chars)d."),
                code='not_enough_digits_and_special_chars',
                params={'min_digits': self.min_digits,
                        'min_special_chars': self.min_special_chars},
            )
        elif digits < self.min_digits:
            raise ValidationError(
                _("Wymagana ilośc cyfr: %(min_digits)d"),
                code='not_enough_digits',
                params={'min_digits': self.min_digits},
            )
        elif special_chars < self.min_special_chars:
            raise ValidationError(
                _("Wymagana ilośc znaków specjalnych: %(min_special_chars)d."),
                code='not_enough_special_chars',
                params={'min_special_chars': self.min_special_chars},
            )

    def get_help_text(self):
        return _(
            "Wymagana ilośc cyfr: %(min_digits)d. Wymagana ilośc specjalnych znaków: %(min_special_chars)d"
            % {'min_digits': self.min_digits,
               'min_special_chars': self.min_special_chars}
        )


