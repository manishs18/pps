import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
def divide(a, b):
    try:
        result = a / b
        logging.info("Division successful.")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error: {e}")
    finally:
        logging.debug("Execution complete.")

print(divide(10, 2)) # Output: 5.0
print(divide(10, 0)) # Logs error and continues execution.