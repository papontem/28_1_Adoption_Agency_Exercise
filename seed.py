from app import db
from models import Pet

db.drop_all()
db.create_all()


pet_1 = Pet( name = 'Princess'  , species = 'pig'  , age = 2  , available = True  , notes = 'Loves food and rolling in mud' )
pet_2 = Pet(name='Buddy', species='tortise', age=50, available=False, notes='Enjoys swimming and basking in the sun')
pet_3 = Pet(name='Max', species='dog', age=5, available=True, notes='Loves hiking in the mountains')

db.session.add_all([pet_1,pet_2,pet_3])
db.session.commit()
