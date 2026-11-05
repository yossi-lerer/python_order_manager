import logging
logger = logging.getLogger(__name__)

def validate_positive_num(num):
    try:
        if int(num) >= 0:
            return True
    except:
        logger.warning(f"A positive integer input was entered: {num}")
        return False