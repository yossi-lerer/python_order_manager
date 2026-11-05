import logging
from manage_system import main_manager
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.txt", level=logging.DEBUG, format="%(levelname)s: %(asctime)s: %(message)s")

def main():
    logger.info("the program started")
    main_manager()

if __name__ == "__main__":
    main()