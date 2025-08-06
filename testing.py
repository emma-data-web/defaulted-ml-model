import logging 

logging.basicConfig(
    level=logging.INFO,  # Log all INFO and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("my_logs.txt", mode='a'),
        logging.StreamHandler()
    ]
)



def man(a,b):
  logging.info('started the fuction!!!')
  try:
    result = a/b
    logging.info(f'trying to divide {a} againt {b} to = {result}')
    logging.warning('pls alway avoid diving by zero')
  except Exception as e:
    logging.error(f'if it didnt work, then this is the error{e}')
    result = None
  return  result

print(man(2,1))

import logging

# 1. Create a custom logger
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)

# 2. Create handlers
file_handler = logging.FileHandler("manual_logs.txt")
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

# 3. Create formatter and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 4. Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)