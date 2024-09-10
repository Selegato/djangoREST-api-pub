from rest_framework import serializers
import re
from datetime import date
from .models import BenefitModel

def validade_document(value):        
        #checa se o cpf tem 11 digitos
        if len(value) != 11:
            raise serializers.ValidationError({'cpf':'CPF deve conter 11 digitos'})
        
        if ' ' in value:
                raise serializers.ValidationError({'cpf':'CPF não deve conter espaços'})
        
        #valida o cpf
        def calculate_digit(digits):
                s = sum(int(digit) * weight for digit, weight in zip(digits, range(len(digits) + 1, 1, -1)))
                remainder = s % 11
                return '0' if remainder < 2 else str(11 - remainder)

        if value[-2:] != calculate_digit(value[:-2]) + calculate_digit(value[:-1]):
                raise serializers.ValidationError({'cpf':'CPF inválido.'})

        return value


def validate_name(value):
    
    # Verifica se o nome contém apenas letras do alfabeto latino e não contém \t ou \n
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', value):
                raise serializers.ValidationError("O nome deve conter apenas letras do alfabeto latino.")
        return value


def validate_birth_date(value):
        # Verifica se a data de nascimento é válida
        if value.year < 1900:
                raise serializers.ValidationError("Data de nascimento inválida.")


        # Calcula a idade do usuário
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        
        # Verifica se o usuário tem pelo menos 18 anos
        if age < 18:
            raise serializers.ValidationError("O usuário deve ter pelo menos 18 anos.")
        
        return value



class CustomerSerializer(serializers.Serializer):
        document = serializers.CharField(validators=[validade_document])
        
        firstName = serializers.CharField(min_length=2,
                                         max_length=50,
                                        validators=[validate_name])
        lastName = serializers.CharField(required=True, 
                                         min_length=2,
                                         max_length=50,
                                         validators=[validate_name])
        
        gender = serializers.ChoiceField(choices=["M", "F"])
        
        email = serializers.EmailField()

        emailSecondary = serializers.EmailField(required=True, allow_blank=True)

        phoneNumber = serializers.CharField(min_length=12, max_length=50) #needs better validation

        birthDate = serializers.DateField(validators=[validate_birth_date])

        registerDate = serializers.DateTimeField(required=False)

        updateDate = serializers.DateTimeField(required=False)

        avatar = serializers.CharField(required=True, allow_blank=True)

        def to_internal_value(self, data):
                data['document'] = re.sub(r'\D', '', data.get('document', ''))
                data['firstName'] = data.get('firstName', '').strip().replace('\t', '').replace('\n', '')
                data['lastName'] = data.get('lastName', '').strip().replace('\t', '').replace('\n', '')
                data['gender'] = data.get('gender', '').upper()
                data['email'] = data.get('email', '').strip().lower()
                data['emailSecondary'] = data.get('emailSecondary', '').strip().lower()
                return super().to_internal_value(data)
        

class BenefitSerializer(serializers.ModelSerializer):
        class Meta:
                model = BenefitModel
                fields = '__all__'