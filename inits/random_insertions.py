import requests
from faker import Faker
import random
from datetime import datetime
from requests.auth import HTTPBasicAuth
import json

fake = Faker('pt_BR')

url = 'http://localhost:8000/api/customers/'
headers = {'Content-Type': 'application/json',
           }



def test_call():
    customer_data = {
        'document': fake.cpf(),
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'gender': random.choice(['M', 'F']),
        'email': fake.email(),
        'emailSecondary': fake.email(),
        'phoneNumber': fake.phone_number(),
        'birthDate': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d'),
        'registerDate': datetime.now().isoformat(),
        'updateDate': datetime.now().isoformat(),
        'deleteFlag': '0',
        'avatar': ''
    }
    response = requests.post(url, data=json.dumps(customer_data), headers=headers, auth=HTTPBasicAuth('admin', 'admin'))

    if response.status_code == 201:
        print('Cliente inserido com sucesso!')
    else:
        print('Falha ao inserir cliente:', response.json())

if __name__ == '__main__':
    for _ in range(50):
        test_call()