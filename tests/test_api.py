from app.api import app

def test_price_endpoint_with_off10():
    client = app.test_client()
    response = client.post('/price', json={
        "price": 100,
        "coupon": "OFF10",
        "tax_rate": 0.19
    })
    assert response.status_code == 200
    assert response.get_json()["final_price"] == 107.1

def test_price_endpoint_without_coupon():
    client = app.test_client()
    response = client.post('/price', json={
        "price": 100,
        "coupon": "",
        "tax_rate": 0.19
    })
    assert response.status_code == 200
    assert response.get_json()["final_price"] == 119.0

def test_price_endpoint_invalid_coupon():
    client = app.test_client()
    response = client.post('/price', json={
        "price": 100,
        "coupon": "INVALID",
        "tax_rate": 0.19
    })
    assert response.status_code == 200
    assert response.get_json()["final_price"] == 119.0
