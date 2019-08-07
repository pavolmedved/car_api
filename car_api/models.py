from car_api import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#init database
db = SQLAlchemy(app)
#init marhsmallow
ma = Marshmallow(app)

#create product model
class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.String(150), unique = True)
    year = db.Column(db.Integer)
    color = db.Column(db.String(50))
    price = db.Column(db.Float)

    def __init__(self,model,year,color,price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

#create product schema
class CarSchema(ma.Schema):
    class Meta:
        fields = ('id','model','year','color','price')

#init schema
car_schema = CarSchema(strict=True)
cars_schema = CarSchema(many=True,strict=True)


#2
class Salesperson(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), unique = True)
    last_name = db.Column(db.String(150))

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

class Salesperson(ma.Schema):
     class Meta:
         fields = ('id','first_name','last_name')

     salesperson_schema = SalespersonSchema(strict=True)
     salespersons_schema = SalespersonSchema(many=True,strict=True)

#3
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firs_name = db.Column(db.String(150), unique = True)
    last_name = db.Column(db.String(150))
    invoice = db.Column(db.Integer)

    def __init__(self,first_name,last_name,invoice):
        self.first_name = first_name
        self.last_name = last_name
        self.invoice = invoice

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id','first_name','last_name','invoice')

customer_schema = CustomerSchema(strict=True)
customers_schema = CustomerSchema(many=True,strict=True)

#4
#create product model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mechanic_name = db.Column(db.String(150), unique = True)
    service_type = db.Column(db.String(300))
    serial = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self,model,year,color,price):
        self.mechanic_name = mechanic_name
        self.service_type = service_type
        self.serial = serial
        self.price = price

#create product schema
class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id','mechanic_name','service_type','serial','price')

#init schema
service_schema = ServiceSchema(strict=True)
services_schema = ServiceSchema(many=True,strict=True)

#5
class Parts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    part_name = db.Column(db.String(150), unique = True)
    service_type = db.Column(db.String(300))
    serial = db.Column(db.Integer)

    def __init__(self,model,year,color):
        self.part_name = part_name
        self.service_type = service_type
        self.serial = serial
        

#create product schema
class PartsSchema(ma.Schema):
    class Meta:
        fields = ('id','part_name','service_type','serial')

#init schema
parts_schema = ServiceSchema(strict=True)
partss_schema = ServiceSchema(many=True,strict=True)

#6
class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firs_name = db.Column(db.String(150), unique = True)
    last_name = db.Column(db.String(150))

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        

class MechanicSchema(ma.Schema):
    class Meta:
        fields = ('id','first_name','last_name')

mechanic_schema = MechanicSchema(strict=True)
mechanics_schema = MechanicSchema(many=True,strict=True)

#7
class Repair(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    repair_name = db.Column(db.String(150), unique = True)
    serial = db.Column(db.Integer)
    mechanic_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)

    def __init__(self,model,year,color,price):
        self.repair_name = repair_name
        self.serial = serial
        self.mechanic_id = mechanic_id
        self.service_id = service_id

#create product schema
class RepairSchema(ma.Schema):
    class Meta:
        fields = ('id','repair_name','serial','mechanic_id','service_id')

#init schema
repair_schema = RepairSchema(strict=True)
repairs_schema = RepairSchema(many=True,strict=True)

#8
class History(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    serial = db.Column(db.Integer)
    mechanic_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)

    def __init__(self,serial,mechanic_id,service_id,customer_id):
        self.serial = serial
        self.mechanic_id = mechanic_id
        self.service_id = service_id
        self.customer_id = customer_id

#create product schema
class HistorySchema(ma.Schema):
    class Meta:
        fields = ('id','serial','mechanic_id','service_id','customer_id')

#init schema
history_schema = HisotrySchema(strict=True)
hisotrys_schema = HisotrySchema(many=True,strict=True)

#9
class Combotable(db.Model):
    mechanic_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)
    part_id = db.Column(db.Integer)

    def __init__(self,mechanic_id,service_id,customer_id,part_id):
        self.mechanic_id = mechanic_id
        self.service_id = service_id
        self.part_id = part_id

#create product schema
class CombotableSchema(ma.Schema):
    class Meta:
        fields = ('mechanic_id','service_id','part_id')

#init schema
combotable_schema = CombotableSchema(strict=True)
combotables_schema = CombotableSchema(many=True,strict=True)






