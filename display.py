def display_list_of_dict(list_dict):
    for indexes in list_dict:
        print("======================")
        for i in indexes:
            print(f"{i}: {indexes[i]}")