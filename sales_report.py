from db.handles_json import get_data_from_json
def make_sales_report():
    data = get_data_from_json("./db/orders.json")
    total = 0
    for products in data:
        if products["status"] == "CLOSED":
            total += products["total"]
    print(len(data))
    print(total)
    
if __name__ == "__main__":
    make_sales_report()