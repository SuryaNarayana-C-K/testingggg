from cart import calculate_total


def test_cart_without_discount():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1},
    ]

    assert calculate_total(items, 0) == 250


def test_cart_with_discount():
    items = [
        {"price": 100, "quantity": 2},
        {"price": 50, "quantity": 1},
    ]

    # 250 - 10% = 225
    assert calculate_total(items, 10) == 225