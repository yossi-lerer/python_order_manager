def validate_positive_num(num):
    try:
        if int(num) >= 0:
            return True
    except:
        return False