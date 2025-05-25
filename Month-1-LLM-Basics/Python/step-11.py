"""
step-11.py
Step 11: Error Handling
"""
import logging
logging.basicConfig(level=logging.INFO)
try:
    x = 1/0
except ZeroDivisionError as e:
    logging.error("Error occurred", exc_info=True)
else:
    print("No error")
finally:
    print("Cleanup")
# Custom exception
class MyError(Exception):
    pass
def fn():
    raise MyError("Oops")
try:
    fn()
except MyError as e:
    print(e)
