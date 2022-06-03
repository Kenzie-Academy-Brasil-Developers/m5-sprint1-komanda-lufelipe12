from .menu import AVAILABLE_MENU

table_tab = list()

def get_item(item_id:int) -> dict:
    for item in AVAILABLE_MENU:
        if item['id'] == item_id:
            return item
        
    return None


def add_item_to_tab(table_tab: list, item_id: int, amount: int) -> bool:
    item = get_item(item_id)

    if not item: 
        return False
    
    table_tab.append(dict(id=item['id'], name=item['name'], price=item['price'], amount=amount))

    return True


def calculate_tab(table_tab:list) -> int:
    sum = 0
    for item in table_tab:
        sum += item['price']*item['amount']

    return sum

