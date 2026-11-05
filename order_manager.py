from db.handles_json import get_data_from_json, add_data_to_json
from user_input import user_input_num
from product_manager import get_product

def generate_order_id():
    data = get_data_from_json("./db/orders.json")
    return data[-1]["id"] + 1

def discount_order(price):
    if 300 <= price < 700:
        price = price * 0.95
        print(f"price after discount {price}, the discount is 5%")
    elif 700 <= price < 1500:
        price = price * 0.90
        print(f"price after discount {price}, the discount is 10%")
    elif price > 1500:
        price = price * 0.85
        print(f"price after discount {price}, the discount is 15%")
    return price

def create_order():

    order = {
    "id": generate_order_id(),
    "items": [],
    "total": 0,
    "status": "OPEN"
    }

    while True:
        order_id = user_input_num("to order please enter product id")
        order_quantity = user_input_num("please enter quantity")     
        is_product_available = False       
        for product in get_product():
            if order_id == product["id"]:
                order["total"] += order_quantity * product["price"]
                order["items"].append({'product_id': order_id, 'quantity': order_quantity})
                is_product_available = True
        if not is_product_available:
            print("product not found")
        finish_order = user_input_num("to finish order please press 0 to continue press 1")
        if finish_order == 0:
            break
    
    print(f'price before discount {order["total"]}')

    order["total"] = discount_order(order["total"])

    if len(order["items"]) != 0:
        add_data_to_json("./db/orders.json",order)
        return order
    else:
        return "dont create order"

def show_all_orders():
    return get_data_from_json("./db/orders.json")

def find_order_by_id(order_id):
    orders = get_data_from_json("./db/orders.json")
    for order in orders:
        if order["id"] == order_id:
            return order
        
def close_order(order_id):
    orders = get_data_from_json("./db/orders.json")
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "CLOSED"
    return orders