from menu import show_menu
from user_input import user_input_num
from product_manager import get_product
from order_manager import show_all_orders, find_order_by_id, close_order, create_order
from sales_report import make_sales_report
from display import display_list_of_dict
from db.handles_json import add_data_to_json, get_data_from_json

def main_manager():
    while True:
        show_menu()
        input_menu = user_input_num("Choose option")
        if input_menu == 1:
            display_list_of_dict(get_product())
            print(create_order())
        if input_menu == 2:
            display_list_of_dict(show_all_orders())
        if input_menu == 3:
            order_id = user_input_num("enter order id")
            display_list_of_dict([find_order_by_id(order_id)])
        if input_menu == 4:
            order_id = user_input_num("enter order id")
            display_list_of_dict(close_order(order_id))
        if input_menu == 5:
            make_sales_report()
        if input_menu == 0:
            break