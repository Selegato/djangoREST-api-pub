from django.db import models
from datetime import datetime
from pymongo import MongoClient

# Função para obter a conexão com o banco de dados
def get_unidata_qa():
    url = 'mongodb://admin:admin@localhost:27017/UniDataQA?authSource=admin'
    client = MongoClient(url)
    db = client['UniDataQA']
    return db

class Customer(models.Model):
    def __init__(self, document, first_name, last_name, gender, email, email_secondary, phone_number, birth_date, avatar=''):
        self.document = document
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.email_secondary = email_secondary
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.avatar = avatar
        self.register_date = datetime.now().isoformat()
        self.update_date = datetime.now().isoformat()

    def to_dict(self):
        return {
            'document': self.document,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'gender': self.gender,
            'email': self.email,
            'emailSecondary': self.email_secondary,
            'phoneNumber': self.phone_number,
            'birthDate': self.birth_date,
            'avatar': self.avatar,
            'registerDate': self.register_date,
            'updateDate': self.update_date,
        }
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class CustomerModel:
    def __init__(self, db):
        self.collection = db['customers']

    def insert_customer(self, customer):
        return self.collection.insert_one(customer)

    def find_customer(self, document):
        return self.collection.find_one({'document': document})
    
    def get_all_customers(self):
        return list(self.collection.find({}))
    
    def update_customer(self, document, customer_data):
        return self.collection.update_one({'document': document}, {'$set': customer_data})

    def delete_customer(self, document):
        return self.collection.delete_one({'document': document})
    
class BenefitModel(models.Model):
    LEVEL_CHOICES = (
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )

    nrCpf = models.CharField(max_length=11, primary_key=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=8)
    points = models.IntegerField()

    def __str__(self):
        return f'{self.nrCpf} - {self.level}'
    
    class Meta:
        db_table = 'customer_benefits'