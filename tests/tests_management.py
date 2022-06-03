from restaurant.management import get_item, add_item_to_tab, calculate_tab

def test_get_item() -> None:
    result = get_item(1)
    assert result == {"id": 1, "name": "ADICIONAL FRANGO 50G", "price": 4.0}, 'Test for getting items'

def test_add_item_to_tab() -> None:
    result = add_item_to_tab([], 1, 1)
    assert result is True

def test_calculate_tab() -> None:
    result = calculate_tab([{"id": 1, "name": "ADICIONAL FRANGO 50G", "price": 4.0, "amount":2}])
    assert result == 8.0

