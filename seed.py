from app import db
from models import Pet

db.drop_all()
db.create_all()


pet_1 = Pet(name='Max', species='dog', age=5, available=True, notes='Loves hiking in the mountains')

db.session.add_all([pet_1])
db.session.commit()
