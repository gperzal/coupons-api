from app.coupons import apply_coupon, calculate_final_price

def test_discount_off10():
    assert apply_coupon(100, "OFF10") == 90.0

def test_discount_super20():
    assert apply_coupon(200, "SUPER20") == 160.0

def test_discount_welcome():
    assert apply_coupon(100, "WELCOME") == 85.0

def test_final_price_with_tax_rate():
    assert calculate_final_price(100, "OFF10", tax_rate=0.19) == 107.1
