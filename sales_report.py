from db.handles_json import get_data_from_json
from display import display_list_of_dict
def make_sales_report():
    data = get_data_from_json("./db/orders.json")
    
    total = 0

    for products in data:
        if products["status"] == "CLOSED":
            total += products["total"]
    
    filter_closed = filter(lambda o: o["status"] == "CLOSED",  data)
    high_price = sorted(filter_closed, key=lambda o: o["total"], reverse=True)   
    if len(data) > 0:
        print(f"total orders: {len(data)}")
        if high_price != []:
            print("The highest-priced order")
            display_list_of_dict([high_price[0]])

            print("The Three Most Expensive Orders")    
            display_list_of_dict(high_price[0:2])
            print(f"the total price of close order: {total}")
        else:
            print("There are no closed orders.")
    else:
        print("There are no orders.")



if __name__ == "__main__":
    make_sales_report()