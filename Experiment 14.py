
import logging


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def divide_numbers(a, b):
    # Record that the function has started
    logging.info("Division function started")

   
    logging.debug("Values received: a=%s, b=%s", a, b)

    try:
       
        result = a / b

      
        logging.info("Division successful")

       
        return result

    except ZeroDivisionError:
       
        logging.exception("Cannot divide by zero")

       
        return None


logging.info("Program started")


print("Result:", divide_numbers(10, 2))


print("Result:", divide_numbers(10, 0))


logging.info("Program finished")


print("Check app.log for execution details.")
