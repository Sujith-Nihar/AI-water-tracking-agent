import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(ascime)s - %(levelname)s - %(message)s"

)

def log_message(message):
    logging.info(message)


def log_error(error):
    logging.error(error)
