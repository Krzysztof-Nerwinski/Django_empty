from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import get_default_password_validators, validate_password
from django.core.exceptions import ValidationError
from django.test import TestCase, Client


class TestUserCreation(TestCase):
    user_model = get_user_model()

    def setUp(self):
        self.normal_user_1 = self.user_model.objects.create_user(email='normal_user@mail.com',
                                                                 first_name='first_name1',
                                                                 last_name='last_name1',
                                                                 password='Haslotestowe1;')

        self.super_user_1 = self.user_model.objects.create_superuser(email='admin_user@mail.com',
                                                                     first_name='admin_name1',
                                                                     last_name='admin_name2',
                                                                     password='Hasloadministratora1;')

        self.normal_user_2 = self.user_model.objects.create_user(email='normal_user2@mail.com',
                                                                 first_name='first_name2',
                                                                 last_name='last_name2',
                                                                 password='haslotestowe')

    def test_user_exists(self):
        self.assertIsNotNone(self.normal_user_1)
        self.assertIsNotNone(self.super_user_1)
        self.assertIsNotNone(self.normal_user_2)

    def test_users(self):
        all_users = self.user_model.objects.all().count()
        self.assertEqual(all_users, 3)

    def test_user_first_name(self):
        self.assertEqual(self.normal_user_1.first_name, 'first_name1')
        self.assertEqual(self.super_user_1.first_name, 'admin_name1')

    def test_user_last_name(self):
        self.assertEqual(self.normal_user_1.last_name, 'last_name1')
        self.assertEqual(self.super_user_1.last_name, 'admin_name2')

    def test_user_email(self):
        self.assertEqual(self.normal_user_1.email, 'normal_user@mail.com')
        self.assertEqual(self.super_user_1.email, 'admin_user@mail.com')

    def test_is_active_status(self):
        self.assertTrue(self.normal_user_1.is_active)
        self.assertTrue(self.super_user_1.is_active)

    def test_is_staff_status(self):
        self.assertFalse(self.normal_user_1.is_staff)
        self.assertTrue(self.super_user_1.is_staff)

    def test_is_superuser_status(self):
        self.assertFalse(self.normal_user_1.is_superuser)
        self.assertTrue(self.super_user_1.is_superuser)

    def test_authentication(self):
        user = authenticate(email=self.normal_user_1.email, password='Haslotestowe1;')
        self.assertIsNotNone(user)
        self.assertTrue(user.is_authenticated)


class TestPasswordValidation(TestCase):
    user_model = get_user_model()

    def setUp(self):
        self.user = self.user_model.objects.create_user(email='normal_user@mail.com',
                                                        first_name='first_name1',
                                                        last_name='last_name1',
                                                        password='Haslotestowe1;')
        self.password_ok = 'Haslotestowe1;'
        self.password_too_short = 'Haslo1;'
        self.password_all_cap = 'HASLOTESTOWE1;'
        self.password_all_small = 'haslotestowe1;;'
        self.password_no_special_sign = 'Haslotestowe1'
        self.password_no_numbers = 'Haslotestowe;;'
        self.password_only_numbers = '123432543654362;'
        self.validators = get_default_password_validators()
        self.messages = {
            'too_short': 'To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków.',
            'not_enough_small': 'Wymagana ilośc małych liter: 1',
            'not_enough_cap': 'Wymagana ilośc dużych liter: 1',
            'no_small_and_cap': 'Wymagana ilośc małych liter: 1',
            'no_spec_signs': 'Wymagana ilośc znaków specjalnych: 1.',
            'no_digits': 'Wymagana ilośc cyfr: 1',
            'common_name': 'Hasło jest zbyt podobne do imię.',
            'only_digits': 'Wymagana ilośc dużych liter: 1 oraz małych liter 1',
        }

    def test_check_validators_amount(self):
        self.assertEqual(len(self.validators), 6)

    def test_correct_password(self):
        passed_if_none = validate_password(self.password_ok)
        self.assertIsNone(passed_if_none)

    def test_pass_too_short(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_too_short)
        self.assertEqual(exc.exception.messages[0], self.messages['too_short'])
        self.assertEqual(exc.exception.error_list[0].code, 'password_too_short')

    def test_pass_not_enough_small_letters(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_all_cap)
        self.assertEqual(exc.exception.messages[0], self.messages['not_enough_small'])
        self.assertEqual(exc.exception.error_list[0].code, 'not_enough_small_letters')

    def test_pass_not_enough_cap_letters(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_all_small)
        self.assertEqual(exc.exception.messages[0], self.messages['not_enough_cap'])
        self.assertEqual(exc.exception.error_list[0].code, 'not_enough_cap_letters')

    def test_pass_not_enough_special_signs(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_no_special_sign)
        self.assertEqual(exc.exception.messages[0], self.messages['no_spec_signs'])
        self.assertEqual(exc.exception.error_list[0].code, 'not_enough_special_chars')

    def test_pass_not_enough_numbers(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_no_numbers)
        self.assertEqual(exc.exception.messages[0], self.messages['no_digits'])
        self.assertEqual(exc.exception.error_list[0].code, 'not_enough_digits')

    def test_only_digits(self):
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.password_only_numbers)
        print(exc.exception.messages)
        print(exc.exception.error_list)
        self.assertEqual(exc.exception.messages[0], self.messages['only_digits'])
        self.assertEqual(exc.exception.error_list[0].code, 'not_enough_cap_and_small_letters')

    def test_common_passwords(self):
        self.assertIsNotNone(self.user)
        with self.assertRaises(ValidationError) as exc:
            validate_password(self.user.first_name, self.user)
        self.assertEqual(exc.exception.messages[0], self.messages['common_name'])
        self.assertEqual(exc.exception.error_list[0].code, 'password_too_similar')



