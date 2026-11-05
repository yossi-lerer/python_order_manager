def display_list_of_dict(list_dict):
    if isinstance(list_dict, list):
        for indexes in list_dict:
            print("======================")
            for i in indexes:
                print(f"{i}: {indexes[i]}")
    else:
        print(list_dict)