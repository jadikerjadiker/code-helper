'''
London Lowmanstone IV
DebugHelper
Version 1.1
12/4/2015
'''

import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format='Debug:%(message)s')

def log(message):
    logging.debug(message)
