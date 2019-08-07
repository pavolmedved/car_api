from car_api import app
from car_api.models import db,car_schema,cars_schema,Car,salesperson_schema,salespersons_schema,Salesperson
from car_api.models import db,customer_schema,customers_schema,Customer,service_schema,services_schema,Service,parts_schema,partss_schema,Parts
from car_api.model import db,mechanic_schema,mechanics_schema,Mechanic,repair_schema,repairs_schema,Repair
from car_api.model import db,hisotry_schema,historys_chema,History,combotable_schema,combotables_schema,Combotable
from flask import request, jsonify

#1
@app.route('/car',methods=['POST'])
def add_car():
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    price = request.json['price']

    new_car = Car(model,year,color,price)

    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)

@app.route('/car/<id>',methods=['GET'])
def get_car(id):
    car =Car.query.get(id)
    return car_schema.jsonify(car)

@app.route('/car/<id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get(id)

    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    price = request.json['price']

    car.model = model
    car.year = year
    car.color = color
    car.price = price

    db.session.commit()

    return car_schema.jsonify(car)

@app.route('/car/<id>', methods=['DELETED'])
def deleted_car(id):
    car = Car.query.get(id)
    db.session.deleted(car)
    db.session.commit()

    return car_schema.jsonify(car)

@app.route('/cars', methods=['GET'])
def get_all_cars():
     all_cars = Car.query.all()
     result = cars_schema.dump(all_cars)
     return jsonify(result.data)


#2
@app.route('/salesperson',methods=['POST'])
def add_salesperson():
    first_name = request.json['first_name']
    last_name = request.json['last_name']

    new_salesperson = Salesperson(first_name,last_name)

    db.session.add(new_salesperson)
    db.session.commit()

    return salesperson_schema.jsonify(new_salesperson)

@app.route('/salesperson/<id>',methods=['GET'])
def get_salesperson(id):
    salesperson =Salesperson.query.get(id)
    return salesperson_schema.jsonify(salesperson)

@app.route('/salesperson/<id>', methods=['PUT'])
def update_salesperson(id):
    salesperson = Salesperson.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']

    salesperson.first_name = first_name
    salesperson.last_name = last_name

    db.session.commit()

    return salesperson_schema.jsonify(salesperson)

@app.route('/salesperson/<id>', methods=['DELETED'])
def deleted_salesperson(id):
    salesperson = Salesperson.query.get(id)
    db.session.deleted(salesperson)
    db.session.commit()

    return salesperson_schema.jsonify(salesperson)

@app.route('/salespersons', methods=['GET'])
def get_all_salespersons():
     all_salespersons = Salesperson.query.all()
     result = salespersons_schema.dump(all_salespersons)
     return jsonify(result.data)

#3
@app.route('/customer',methods=['POST'])
def add_customer():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    invoice = request.json['invoice']

    new_customer = Customer(first_name,last_name,invoice)

    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)

@app.route('/customer/<id>',methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    return customer_schema.jsonify(customer)

@app.route('/customer/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    invoice = request.json['invoice']
    
    customer.first_name = first_name
    customer.last_name = last_name
    customer.invoice = invoice

    db.session.commit()

    return customer_schema.jsonify(customer)

@app.route('/customer/<id>', methods=['DELETED'])
def deleted_customer(id):
    customer = Customer.query.get(id)
    db.session.deleted(customer)
    db.session.commit()

    return customer_schema.jsonify(customer)

@app.route('/customers', methods=['GET'])
def get_all_customers():
     all_customers = Customer.query.all()
     result = customers_schema.dump(all_customers)
     return jsonify(result.data)

#4
@app.route('/service',methods=['POST'])
def add_service():
    mechanic_name = request.json['mechanic_name']
    service_type = request.json['service_type']
    serial = request.json['serial']
    price = request.json['price']

    new_service = Service(mechanic_name,service_type,serial,price)

    db.session.add(new_service)
    db.session.commit()

    return service_schema.jsonify(new_service)

@app.route('/service/<id>',methods=['GET'])
def get_service(id):
    service = Service.query.get(id)
    return service_schema.jsonify(service)

@app.route('/service/<id>', methods=['PUT'])
def update_service(id):
    service = Service.query.get(id)

    mechanic_name = request.json['mechanic_name']
    service_type = request.json['service_type']
    serial = request.json['serial']
    price = request.json['price']

    service.mechanic_name = mechanic_name
    service.service_type = service_type
    service.serial = serial
    service.price = price

    db.session.commit()

    return service_schema.jsonify(service)

@app.route('/service/<id>', methods=['DELETED'])
def deleted_service(id):
    service = service.query.get(id)
    db.session.deleted(service)
    db.session.commit()

    return service_schema.jsonify(service)

@app.route('/services', methods=['GET'])
def get_all_services():
     all_services = Service.query.all()
     result = services_schema.dump(all_services)
     return jsonify(result.data)

#5
@app.route('/parts',methods=['POST'])
def add_parts():
    part_name = request.json['part_name']
    service_type = request.json['service_type']
    serial = request.json['serial']

    new_parts = parts(part_name,service_type,serial)

    db.session.add(new_parts)
    db.session.commit()

    return service_schema.jsonify(new_parts)

@app.route('/parts/<id>',methods=['GET'])
def get_parts(id):
    parts = Parts.query.get(id)
    return parts_schema.jsonify(parts)

@app.route('/parts/<id>', methods=['PUT'])
def update_parts(id):
    parts = Parts.query.get(id)

    part_name = request.json['part_name']
    service_type = request.json['service_type']
    serial = request.json['serial']

    parts.part_name = part_name
    parts.service_type = service_type
    parts.serial = serial
    parts.price = price

    db.session.commit()

    return parts_schema.jsonify(parts)

@app.route('/parts/<id>', methods=['DELETED'])
def deleted_parts(id):
    parts = Parts.query.get(id)
    db.session.deleted(parts)
    db.session.commit()

    return parts_schema.jsonify(parts)

@app.route('/partss', methods=['GET'])
def get_all_partss():
     all_partss = Parts.query.all()
     result = partss_schema.dump(all_partss)
     return jsonify(result.data)

#6
@app.route('/mechanic',methods=['POST'])
def add_mechanic():
    first_name = request.json['first_name']
    last_name = request.json['last_name']

    new_mechanic = Mechanic(first_name,last_name)

    db.session.add(new_mechanic)
    db.session.commit()

    return mechanic_schema.jsonify(new_mechanic)

@app.route('/mechanic/<id>',methods=['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get(id)
    return mechanic_schema.jsonify(mechanic)

@app.route('/mechanic/<id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get(id)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    
    mechanic.first_name = first_name
    mechanic.last_name = last_name

    db.session.commit()

    return mechanic_schema.jsonify(mechanic)

@app.route('/mechanic/<id>', methods=['DELETED'])
def deleted_mechanic(id):
    mechanic = Mechanic.query.get(id)
    db.session.deleted(mechanic)
    db.session.commit()

    return mechanic_schema.jsonify(mechanic)

@app.route('/mechanics', methods=['GET'])
def get_all_mechanics():
     all_mechanics = Mechanic.query.all()
     result = mechanics_schema.dump(all_mechanics)
     return jsonify(result.data)

#7
@app.route('/repair',methods=['POST'])
def add_repair():
    repair_name = request.json['repair_name']
    serial = request.json['serial']
    mechanic_id = request.json['mechanic_id']
    service_id = request.json['service_id']

    new_repair = Repair(repair_name,serial,mechanic_id,service_id)

    db.session.add(new_repair)
    db.session.commit()

    return repair_schema.jsonify(new_repair)

@app.route('/repair/<id>',methods=['GET'])
def get_repair(id):
    repair = Repair.query.get(id)
    return repair_schema.jsonify(repair)

@app.route('/repair/<id>', methods=['PUT'])
def update_repair(id):
    repair = Repair.query.get(id)

    repair_name = request.json['repair_name']
    serial = request.json['serial']
    mechanic_id = request['mechanic_id']
    service_id = request['service_id']
    
    repair.repair_name = repair_name
    repair.serial = serial
    repair.mechanic_id = mechanic_id
    repair.service_id = service_id

    db.session.commit()

    return repair_schema.jsonify(repair)

@app.route('/repair/<id>', methods=['DELETED'])
def deleted_repair(id):
    repair = Repair.query.get(id)
    db.session.deleted(repair)
    db.session.commit()

    return repair_schema.jsonify(repair)

@app.route('/repairs', methods=['GET'])
def get_all_repairs():
     all_repairs = Repair.query.all()
     result = repairs_schema.dump(all_repairs)
     return jsonify(result.data)
#8
@app.route('/history',methods=['POST'])
def add_history():
    serial = request.json['serial']
    mechanic_id = request.json['mechanic_id']
    service_id = request.json['service_id']
    customer_id = request.json['customer_id']

    new_histroy = History(serial,mechanic_id,service_id,customer_id)

    db.session.add(new_history)
    db.session.commit()

    return history_schema.jsonify(new_history)

@app.route('/history/<id>',methods=['GET'])
def get_history(id):
    history = History.query.get(id)
    return hisotry_schema.jsonify(hisotry)

@app.route('/history/<id>', methods=['PUT'])
def update_hisotry(id):
    hisotry = History.query.get(id)

    serial = request.json['serial']
    mechanic_id = request.json['mechanic_id']
    service_id = request.json['service_id']
    customer_id = request.json['customer_id']

    history.serial = serial
    hisotry.mechanic_id = mechanic_id
    hisotry.service_id = service_id
    hisotry.customer_id = customer_id

    db.session.commit()

    return history_schema.jsonify(hisotry)

@app.route('/history/<id>', methods=['DELETED'])
def deleted_history(id):
    history = History.query.get(id)
    db.session.deleted(history)
    db.session.commit()

    return hisotry_schema.jsonify(history)

@app.route('/historys', methods=['GET'])
def get_all_hisotrys():
     all_hystorys = History.query.all()
     result = hystorys_schema.dump(all_historys)
     return jsonify(result.data)

#9
@app.route('/combotable',methods=['POST'])
def add_combotable():
    mechanic_id = request.json['mechanic_id']
    service_id = request.json['service_id']
    part_id = request.json['part_id']

    new_combotable = Combotable(mechanic_id,service_id,part_id)

    db.session.add(new_coombotable)
    db.session.commit()

    return combotable_schema.jsonify(new_combotable)

@app.route('/combotable/<id>',methods=['GET'])
def get_combotable(id):
    combotable = Coombotable.query.get(id)
    return combotable_schema.jsonify(combotable)

@app.route('/combotable/<id>', methods=['PUT'])
def update_combotable(id):
    combotable = Combotable.query.get(id)

    mechanic_id = request['mechanic_id']
    service_id = request['service_id']
    part_id = request['part_id']

    combotable.mechanic_id = mechanic_id
    coombotable.service_id = service_id
    combotable.part_id = part_id

    db.session.commit()

    return combotable_schema.jsonif(combotable)

@app.route('/combotable/<id>', methods=['DELETED'])
def deleted_combotable(id):
    combotable = Combotable.query.get(id)
    db.session.deleted(combotable)
    db.session.commit()

    return combotable_schema.jsonify(combotable)

@app.route('/combotables', methods=['GET'])
def get_all_coombotables():
     all_combotables = Combotable.query.all()
     result = combotables_schema.dump(all_combotable)
     return jsonify(result.data)
