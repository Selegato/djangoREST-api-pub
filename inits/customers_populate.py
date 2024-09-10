from faker import Faker
import random
from datetime import datetime
import sys, os
import time

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from mongodb_connection import get_unidata_qa

fake = Faker('pt_BR')

def delete_all(db):
    db.customers.delete_many({})
    db.addresses.delete_many({})
    db.subsidiaries.delete_many({})
    print('All data deleted from the TEST database')

def populate_customers(db, num_users = 500):
    users = []

    print(f'--------USERS BEGIN--------')
    for _ in range(num_users):
        user = {
            'document': fake.cpf(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'gender': random.choice(['1', '2']),
            'email': fake.email(),
            'emailSecondary': fake.email(),
            'phoneNumber': fake.phone_number(),
            'birthDate': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d-%m-%Y'),
            'registerDate': datetime.now().isoformat(),
            'updateDate': datetime.now().isoformat(),
            'deleteFlag': '0',
            'avatar': ''
        }
        users.append(user)
    result = db.customers.insert_many(users)
    print(f'--------USERS END--------')


def populate_all_test(db, num_users = 500): #5k
    print('--------------QA Populate started --------------')

    start_time = time.time()
    users = []

    print(f'--------USERS BEGIN--------')
    for _ in range(num_users):
        user = {
            'document': fake.cpf(),
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'gender': random.choice(['1', '2']),
            'email': fake.email(),
            'emailSecondary': fake.email(),
            'phoneNumber': fake.phone_number(),
            'birthDate': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d-%m-%Y'),
            'registerDate': datetime.now().isoformat(),
            'updateDate': datetime.now().isoformat(),
            'deleteFlag': '0',
            'avatar': ''
        }
        users.append(user)
    result = db.customers.insert_many(users)
    print(f'--------USERS END--------')

    users_ids = result.inserted_ids

    print(f'--------ADRESSES BEGIN--------')
    count_addresses = 0
    for user_id in users_ids:
        addresses = []
        adresses_number = random.randint(1, 3)
        count_addresses += adresses_number
        for _ in range(adresses_number):
            address = {
                'user_id': user_id,
                'addressName': fake.street_name(),
                'addressType': random.choice(['Residencial', 'Comercial']),
                'city': fake.city(),
                'complement': random.choice(['Casa', 'Apartamento']),
                'country': 'BR',
                'geoCoordinate': [float(fake.latitude()), float(fake.longitude())],
                'neighborhood': fake.bairro(),
                'number': fake.building_number(),
                'postalCode': fake.postcode(),
                'receiverName': fake.name(),
                'reference': fake.street_suffix(),
                'state': fake.state_abbr(),
                'street': fake.street_name(),
                'createdIn': datetime.now().isoformat(),
                'updatedIn': datetime.now().isoformat(),
                'lastInteractionIn': datetime.now().isoformat(),
                'defaultFlag': True
            }
            addresses.append(address)
        db.addresses.insert_many(addresses)
    print(f'--------ADRESSES END--------')


    subsidiary_ALUZIC = {
        'subsidiaryId': '27bc40b3-c40e-44db-aaa1-aac9d4565f05',
        'subsidiaryName': 'ALUZIC',
        'registerDate': datetime.now().isoformat(),
        'updateDate': datetime.now().isoformat(),
        'receiveEmailFlag': random.choice(['0', '1']),
        'receiveAppFlag': random.choice(['0', '1']),
        'authorizeDataFlag': random.choice(['0', '1']),
        'favoriteStoreId': str(random.randint(1, 500)),
        'crmUserId': str(fake.uuid4()),
        'prime': random.choice([True, False])
    }        
    subsidiary_MERCAPAI = {
        'subsidiaryId': '461073f1-49ec-49cf-be7b-4b79f604c30d',
        'subsidiaryName': 'MERCAPAI',
        'registerDate': datetime.now().isoformat(),
        'updateDate': datetime.now().isoformat(),
        'receiveEmailFlag': random.choice(['0', '1']),
        'receiveAppFlag': random.choice(['0', '1']),
        'authorizeDataFlag': random.choice(['0', '1']),
        'favoriteStoreId': str(random.randint(1, 500)),
        'crmUserId': str(fake.uuid4()),
        'prime': False
    }        
    subsidiary_ZUQUINI = {
        'subsidiaryId': '323fcd49-475f-49c9-a98b-c0c7ed7cd4ba',
        'subsidiaryName': 'ZUQUINI',
        'registerDate': datetime.now().isoformat(),
        'updateDate': datetime.now().isoformat(),
        'receiveEmailFlag': random.choice(['0', '1']),
        'receiveAppFlag': random.choice(['0', '1']),
        'authorizeDataFlag': random.choice(['0', '1']),
        'favoriteStoreId': str(random.randint(1, 500)),
        'crmUserId': str(fake.uuid4()),
        'prime': False
    }

    print(f'--------SUBSIDIARIES BEGIN--------')
    counter_subs = 0
    for user_id in users_ids:
        nro_subsidiaries = random.randint(1, 3)
        counter_subs += nro_subsidiaries
        subsidiaries = []
        if nro_subsidiaries >= 1:
            subsidiary_ALUZIC['userId'] = user_id
            subsidiaries.append(subsidiary_ALUZIC.copy())
        if nro_subsidiaries >= 2:
            subsidiary_MERCAPAI['userId'] = user_id
            subsidiaries.append(subsidiary_MERCAPAI.copy())
        if nro_subsidiaries == 3:
            subsidiary_ZUQUINI['userId'] = user_id
            subsidiaries.append(subsidiary_ZUQUINI.copy())
        
        if nro_subsidiaries == 1:
            db.subsidiaries.insert_one(subsidiaries[0])
        else:
            db.subsidiaries.insert_many(subsidiaries)
    print(f'--------SUBSIDIARIES END--------')
    end_time = time.time()
    elapsed_time_seconds = end_time - start_time
    elapsed_time_minutes = elapsed_time_seconds / 60
    total_data_generated = num_users + count_addresses + counter_subs

    print(f'--------{num_users} users added to the TEST database--------')
    print(f'--------{count_addresses} addresses added to the TEST database--------')
    print(f'--------{counter_subs} subsidiaries added to the TEST database--------')
    print(f'--------{total_data_generated} records--------')
    print(f'--------{elapsed_time_minutes} minutes--------')
    print(f'--------{elapsed_time_seconds} seconds--------')
    print('--------------QA Populate completed --------------')



if __name__ == '__main__':
    db = get_unidata_qa()
    delete_all(db)
    #populate_customers(db)
    #populate_all_test(db)


