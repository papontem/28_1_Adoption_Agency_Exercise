from app import db
from models import Pet

db.drop_all()
db.create_all()


pet_1 = Pet( name = 'Princess'  , species = 'pig'  , age = 2  , available = True  , notes = 'Loves food and rolling in mud',
            photo_url='https://images.unsplash.com/photo-1636581563722-107ba7a408ad?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1970&q=80' )
pet_2 = Pet(name='Buddy', species='tortise', age=50, available=False, notes='Enjoys swimming and basking in the sun', 
            photo_url='https://images.unsplash.com/photo-1519554394232-0ff1b0cea832?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2340&q=80')

pet_3 = Pet(name='Max', species='dog', age=5, available=True, notes='Loves hiking in the mountains')

db.session.add_all([pet_1,pet_2,pet_3])
db.session.commit()
