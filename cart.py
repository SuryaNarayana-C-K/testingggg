def calculate_total(items, discount_percent):
    """
    Calculate the final shopping cart total.

    items: list of dictionaries with a 'price' and 'quantity'
    discount_percent: percentage discount
    """
    subtotal = sum(item["price"] * item["quantity"] for item in items)

    # BUG: discount is added instead of subtracted
    discount = subtotal * (discount_percent / 100)

    total = subtotal - discount

    return round(total, 2)