#!/bin/bash

BASE_URL="http://localhost:5000/api"

echo "Testing User Registration"
curl -X POST $BASE_URL/register \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "testuser@example.com", "password": "testpassword"}'
echo -e "\n"

echo "Testing User Login"
curl -X POST $BASE_URL/login \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpassword"}'
echo -e "\n"

echo "Testing Add Vehicle"
curl -X POST $BASE_URL/vehicles \
     -H "Content-Type: application/json" \
     -d '{"model": "Tesla Model 3", "battery_capacity": 75.0, "current_charge": 65.0, "user_id": 1}'
echo -e "\n"

echo "Testing Create Route"
curl -X POST $BASE_URL/routes \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "start_latitude": -6.2088, "start_longitude": 106.8456, "end_latitude": -6.1751, "end_longitude": 106.8650, "distance": 10.5, "estimated_duration": 30, "estimated_energy_consumption": 5.2}'
echo -e "\n"

echo "Testing Get Charging Stations"
curl "$BASE_URL/charging_stations?lat=-6.2088&lon=106.8456&radius=5"
echo -e "\n"