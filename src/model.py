from peewee import *

DATABASE = 'amazonas.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class Rol(BaseModel):
    id = IntegerField(unique=True)
    description = CharField()
  
class User(BaseModel):
    username = CharField(unique=True)
    email = CharField()
    password = CharField()
    phone = CharField()
    address = CharField()
    rol_id = ForeignKeyField(Rol)

class Product(BaseModel):
    id = IntegerField(unique=True)
    name = CharField()
    description = CharField()
    price = DecimalField(decimal_places=2)

class Token(BaseModel):
    token = CharField(unique=True)

def create_tables():
    with database:
        database.create_tables([Rol, User, Product, Token])