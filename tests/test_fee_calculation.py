import httpx

def test_fee_calculation():
    response = httpx.post("http://localhost:8000/calculate-fee/", json={"distance_km": 10, "weight_kg": 2})
    assert response.status_code == 200
    assert "delivery_fee" in response.json()

def test_fee_calculation_bad_input():
    response = httpx.post("http://localhost:8000/calculate-fee/", json={"distance_km": "ten", "weight_kg": 2})
    assert response.status_code == 422  # Unprocessable Entity for bad input