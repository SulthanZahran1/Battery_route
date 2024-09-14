from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    vehicles = db.relationship('Vehicle', backref='owner', lazy='dynamic')

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(64))
    battery_capacity = db.Column(db.Float)
    current_charge = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ChargingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    charger_type = db.Column(db.String(64))
    availability = db.Column(db.Boolean)
    pricing = db.Column(db.String(120))
    operational_hours = db.Column(db.String(120))

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_latitude = db.Column(db.Float)
    start_longitude = db.Column(db.Float)
    end_latitude = db.Column(db.Float)
    end_longitude = db.Column(db.Float)
    distance = db.Column(db.Float)
    estimated_duration = db.Column(db.Integer)  # in minutes
    estimated_energy_consumption = db.Column(db.Float)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user = db.relationship('User', backref='routes')