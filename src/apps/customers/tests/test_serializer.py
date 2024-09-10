from django.test import TestCase
from apps.customers.serializers import CustomerSerializer

class TestCustomerSerializer(TestCase):
    def setUp(self):
        self.valid_data = {
            'document': '123.456.789-09',
            'firstName': 'João',
            'lastName': 'Silva',
            'gender': 'M',
            'email': 'joao.silva@example.com',
            'emailSecondary': 'joao.secondary@example.com',
            'phoneNumber': '+55 35 99153-5567',
            'birthDate': '1990-01-01',
            'avatar': ''
        }
    
    def test_valid_document_sem_separador(self):
        self.valid_data['document'] = '11002554608'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_valid_document_com_separador(self):
        self.valid_data['document'] = '110.025.546-08'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_document_missing(self):
        data_without_document = self.valid_data.copy()
        del data_without_document['document']
        serializer = CustomerSerializer(data=data_without_document)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document_empty(self):
        self.valid_data['document'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document(self):
        self.valid_data['document'] = 'invalid_document'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document_letter(self):
        self.valid_data['document'] = 'ABC.DEF.GHI-JK'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document_cyrilic(self):
        self.valid_data['document'] = 'АБВ.ГДЕ.ЖЗИ-КЛ'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document_less(self):
        self.valid_data['document'] = '123.456.789'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_document_more(self):
        self.valid_data['document'] = '123.456.789-0987'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())


#END DOCUMENT

    def test_valid_first_name(self):
        self.valid_data['firstName'] = 'João'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_first_name_empty(self):
        self.valid_data['firstName'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_first_name_missing(self):
        data_without_first_name = self.valid_data.copy()
        del data_without_first_name['firstName']
        serializer = CustomerSerializer(data=data_without_first_name)
        self.assertFalse(serializer.is_valid())

    def test_invalid_first_name_too_short(self):
        self.valid_data['firstName'] = 'J'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_first_name_too_long(self):
        self.valid_data['firstName'] = 'J' * 51
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_first_name_with_invalid_characters(self):
        self.valid_data['firstName'] = 'João123'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_valid_first_name_with_extra_spaces(self):
        self.valid_data['firstName'] = '  João antonio '
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['firstName'], 'João antonio')

    def test_first_name_with_tabs(self):
        self.valid_data['firstName'] = 'João\t'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['firstName'], 'João')

#END NAME

    def test_valid_gender(self):
        self.valid_data['gender'] = 'M'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_valid_gender_lower(self):
        self.valid_data['gender'] = 'f'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['gender'], 'F')

    def test_invalid_gender_missing(self):
        data_without_gender = self.valid_data.copy()
        del data_without_gender['gender']
        serializer = CustomerSerializer(data=data_without_gender)
        self.assertFalse(serializer.is_valid())

    def test_invalid_gender_empty(self):
        self.valid_data['gender'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_gender_invalid(self):
        self.valid_data['gender'] = 'T'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_gender_invalid_extra(self):
        self.valid_data['gender'] = 'LG'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

#END GENDER

    def test_valid_email(self):
        self.valid_data['email'] = 'valid.email@example.com'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_email_missing(self):
        data_without_email = self.valid_data.copy()
        del data_without_email['email']
        serializer = CustomerSerializer(data=data_without_email)
        self.assertFalse(serializer.is_valid())

    def test_invalid_email_empty(self):
        self.valid_data['email'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_email_invalid(self):
        self.valid_data['email'] = 'invalid-email'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_email_cyrilic(self):
        self.valid_data['email'] = 'вфцівфці@вфці.вфці'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())    
        
    def test_invalid_email_spaces(self):
        self.valid_data['email'] = 'pa ulo@te ste.com'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

#END EMAIL

    def test_phone_number_missing(self):
        data_without_phone = self.valid_data.copy()
        del data_without_phone['phoneNumber']
        serializer = CustomerSerializer(data=data_without_phone)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phoneNumber', serializer.errors)

    def test_phone_number_empty(self):
        self.valid_data['phoneNumber'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phoneNumber', serializer.errors)

    def test_phone_number_too_short(self):
        self.valid_data['phoneNumber'] = '1234567890'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phoneNumber', serializer.errors)

    def test_phone_number_too_long(self):
        self.valid_data['phoneNumber'] = '1' * 51
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phoneNumber', serializer.errors)

    def test_phone_number_valid(self):
        self.valid_data['phoneNumber'] = '123456789012'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
#END PHONE NUMBER

    def test_birth_date_missing(self):
        data_without_birth_date = self.valid_data.copy()
        del data_without_birth_date['birthDate']
        serializer = CustomerSerializer(data=data_without_birth_date)
        self.assertFalse(serializer.is_valid())
        self.assertIn('birthDate', serializer.errors)

    def test_birth_date_empty(self):
        self.valid_data['birthDate'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('birthDate', serializer.errors)

    def test_birth_date_invalid(self):
        self.valid_data['birthDate'] = 'invalid-date'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('birthDate', serializer.errors)


    def test_birth_date_invalid_year(self):
        self.valid_data['birthDate'] = '1800-01-01'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_birth_date_less_18years(self):
        self.valid_data['birthDate'] = '2020-01-01'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())

    def test_birth_date_valid(self):
        self.valid_data['birthDate'] = '2000-01-01'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

#END BIRTH DATE --------------NEEDS BETTER TESTS----------------

    def test_avatar_missing(self):
        data_without_avatar = self.valid_data.copy()
        del data_without_avatar['avatar']
        serializer = CustomerSerializer(data=data_without_avatar)
        self.assertFalse(serializer.is_valid())
        self.assertIn('avatar', serializer.errors)

    def test_avatar_empty(self):
        self.valid_data['avatar'] = ''
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_avatar_valid(self):
        self.valid_data['avatar'] = 'http://example.com/avatar.jpg'
        serializer = CustomerSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())