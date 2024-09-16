from flask import jsonify, request
from app import app, db
from app.models import User, Vehicle, ChargingStation, Route
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Logged in successfully', 'user_id': user.id}), 200
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    vehicle = Vehicle(model=data['model'], battery_capacity=data['battery_capacity'],
                      current_charge=data['current_charge'], user_id=data['user_id'])
    db.session.add(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle added successfully', 'vehicle_id': vehicle.id}), 201

@app.route('/api/routes', methods=['POST'])
def create_route():
    data = request.json
    route = Route(user_id=data['user_id'], start_latitude=data['start_latitude'],
                  start_longitude=data['start_longitude'], end_latitude=data['end_latitude'],
                  end_longitude=data['end_longitude'], distance=data['distance'],
                  estimated_duration=data['estimated_duration'],
                  estimated_energy_consumption=data['estimated_energy_consumption'])
    db.session.add(route)
    db.session.commit()
    return jsonify({'message': 'Route created successfully', 'route_id': route.id}), 201

@app.route('/api/charging_stations', methods=['GET'])
def get_charging_stations():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    radius = request.args.get('radius', default=5, type=float)  # km
    
    # This is a simple distance calculation. For more accurate results,
    # you might want to use a geographic library like GeoPy.
    stations = ChargingStation.query.filter(
        (ChargingStation.latitude - lat)**2 + (ChargingStation.longitude - lon)**2 <= (radius/111)**2
    ).all()
    
    return jsonify([{
        'id': station.id,
        'name': station.name,
        'latitude': station.latitude,
        'longitude': station.longitude,
        'charger_type': station.charger_type,
        'availability': station.availability,
        'pricing': station.pricing,
        'operational_hours': station.operational_hours
    } for station in stations])