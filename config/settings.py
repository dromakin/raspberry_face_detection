import os
import logging

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config')
DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'db')

# print(ROOT_DIR)
# print(SETTINGS_DIR)

DEBUG = False

# # logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# # Create a custom logger
# logger = logging.getLogger(__file__)
#
# # Create handlers
# i_handler = logging.FileHandler(os.path.join(ROOT_DIR, "info.log"))
# c_handler = logging.FileHandler(os.path.join(ROOT_DIR, "warnings.log"))
# f_handler = logging.FileHandler(os.path.join(ROOT_DIR, "errors.log"))
# i_handler.setLevel(logging.INFO)
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)
#
# # Create formatters and add it to handlers
# i_format = logging.Formatter('%(asctime)s - %(message)s')
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# i_handler.setFormatter(i_format)
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
#
# # Add handlers to the logger
# logger.addHandler(i_handler)
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
#
# # logger.warning('This is a warning')
# # logger.error('This is an error')
