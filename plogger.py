# import logging    # by default level - warning

# logging.debug("this debug level")
# logging.info("this debug level")
# logging.warning("this debug level")
# logging.error("this debug level")
# logging.critical("this debug level")


# LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\First_log.log"   # First_log.log this is a file name

# logging.basicConfig(format="%(asctime)s----%(name)s--%(process)i--[%(levelname)s]----%(message)s", 
#                     filename=LOGGER_FILE_PATH, level=logging.NOTSET,datefmt='%d-%m-%y %I:%M:%S %p')  # ji level set karu tithn pudhe entry record hotil

# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")


# NAME = input("Enter your name:- ").upper()
# try:
#     logging.info("your task started.....!")
#     logging.debug(NAME)
#     inp1 = int(input("Enter your first number:- "))
#     inp2 = int(input("Enter your second number:- "))
#     logging.debug(f"first value:- {inp1}")
#     logging.debug(f"second value:- {inp2}")
#     print(inp1/inp2)
#     logging.info("your task completed.......!")

# except Exception as msg:
#     logging.error(msg, exc_info=False)       # exc_info it give a traceback msg if True

# ---------------------------------------------------------------------------------------------------------------------------

# user defined logger:-


# LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\handler_log.log"
# logger = logging.getLogger(__name__)

# c_handler = logging.StreamHandler()
# logger.setLevel(logging.DEBUG)

# f_handler = logging.FileHandler(LOGGER_FILE_PATH)

# c_format = logging.Formatter("%(asctime)s---%(process)d---[%(levelname)s]---%(message)s")
# f_format = logging.Formatter("%(asctime)s---%(process)i---[%(levelname)s]---%(message)s")

# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# logger.addHandler(c_handler)
# logger.addHandler(f_handler)

# logger.debug("this is debug")
# logger.info("this is info")
# logger.warning("this is warning")
# logger.error("this is error")
# logger.critical("this is critical")


# --------------------------------------------------------------------------------------------------------------------

# practise:-

# 1.by default:-



# import logging

# LOGGER_FILE_PATH =r"F:\Python(Rohit)\python_logger\practise_log.log"

# logging.basicConfig(format="%(asctime)s---%(name)s---%(process)i---[%(levelname)s]---%(message)s", 
#                     filename=LOGGER_FILE_PATH, level=logging.NOTSET)


# logging.debug("This is debug")
# logging.info("This is info")
# logging.warning("This is warning")
# logging.error("This is error")
# logging.critical("This is critical")


# NAME = input("Enter your name:- ")
# try:
#     logging.info("your task started.......!")
#     logging.debug(NAME)
#     Emp1 = int(input("Enter first number:- "))
#     Emp2 = int(input("Enter second number:- "))
#     logging.debug(f"First value:- {Emp1}")
#     logging.debug(f"Second value:- {Emp2}")
#     logging.debug(f"result:- {Emp1/Emp2}")
#     print(Emp1/Emp2)
#     logging.info("your task completed...........!")

# except Exception as msg:
#     logging.error(msg)



# 2. user defined:-

"""
LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_user_defined.log"
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOGGER_FILE_PATH)

c_format = logging.Formatter("%(asctime)s---[%(levelname)s]---%(message)s")
f_format = logging.Formatter("%(asctime)s---%(process)i---[%(levelname)s]---%(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)


logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")

"""                                          # for commend

# ------------------------------------------------------------------------------------------------------------------------------------

# Rotating handler:-

"""
import logging


from logging.handlers import RotatingFileHandler

LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\rotate_handler.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

rotate_handler = RotatingFileHandler(LOGGER_FILE_PATH, maxBytes=130, backupCount=10)
rotate_handler.setLevel(logging.DEBUG)


Formatter = logging.Formatter("%(asctime)s---[%(levelname)s]---%(message)s")

rotate_handler.setFormatter(Formatter)

logger.addHandler(rotate_handler)

logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")

"""

# ----------------------------------------------------------------------------------------------------------------------------------

# timed_rotating_handler:-

"""
CREATE_LOGGER_FILE = r"F:\Python(Rohit)\python_logger\timed_rotating.log"
import logging

from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

timed_rotating_handler = TimedRotatingFileHandler(CREATE_LOGGER_FILE, when = "S", interval=2, backupCount=10)
timed_rotating_handler.setLevel(logging.DEBUG)


formatter = logging.Formatter("%(asctime)s---%(levelname)s---%(message)s")

timed_rotating_handler.setFormatter(formatter)

logger.addHandler(timed_rotating_handler)


import time
a = time.time()
for i in range(1,10):
    logger.info(f"------{i}------")                 # for info perpose only
    logger.debug("This is debug")
    logger.info("This is info")
    logger.warning("This is warning")
    logger.error("This is error")
    logger.critical("This is critical")
    time.sleep(1)
b = time.time()                          # for time calculation perpose
print(b-a)


"""
# -------------------------------------------------------------------------------------------------------------------------------


# using config file:-

"""
import logging

import logging.config


logging.config.fileConfig(r"F:\Python(Rohit)\python_logger\file.conf", disable_existing_loggers=True)

logger = logging.getLogger(__name__)

logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")


"""
# ---------------------------------------------------------------------------------------------------------------------------



# Rivison:-

# by default:- 


# LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"
# import logging


# logging.basicConfig(format="%(asctime)s----[%(levelname)s]----%(process)i----%(message)s", 
#                     filename=LOGGER_FILE_PATH, level = logging.DEBUG)



# logging.debug("This is debug")
# logging.info("This is info")
# logging.warning("This is warning")
# logging.error("This is error")
# logging.critical("This is critical")


# NAME = input("Enter your name:- ")

# try:
#     logging.info("your task started.............!")
#     logging.debug(NAME)
#     Emp1 = int(input("Enter first number:- "))
#     Emp2 = int(input("Enter second name:- "))
#     logging.info(f"Enter first value:- {Emp1}")
#     logging.info(f"Enter second value:- {Emp2}")
#     logging.debug(f"result:- {Emp1/Emp2}")
#     logging.info("your task ended..............!")
# except Exception as msg:
#     logging.error(msg)


# --------------------------------------------------------------------------------------------------------------------------------

    
# user defined:- 


"""

import logging

LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOGGER_FILE_PATH)


c_format = logging.Formatter("%(asctime)s---[%(levelname)s]---%(message)s")
f_format = logging.Formatter("%(asctime)s---%(process)i---[%(levelname)s]---%(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)


logger.addHandler(c_handler)
logger.addHandler(f_handler)



logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")

"""

# -----------------------------------------------------------------------------------------------------------------------------


# Rotating handler:-

"""


import logging

LOGGER_DFILE_PATH = r"F:\Python(Rohit)\python_logger\rotate_handler.log"
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


rotate_handler = RotatingFileHandler(LOGGER_DFILE_PATH, maxBytes=70, backupCount=10)

formatter = logging.Formatter("%(asctime)s---%(levelname)s---%(message)s")

rotate_handler.setFormatter(formatter)

logger.addHandler(rotate_handler)


logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")



"""

# ----------------------------------------------------------------------------------------------------------------------


# timed_rotating_handler:-



# import logging

# LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"

# logging.basicConfig(format="%(asctime)s---%(levelname)s---%(process)i---%(message)s", 
#                     filename = LOGGER_FILE_PATH, level=logging.DEBUG)


# logging.debug("this is debugg")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")


# NAME = input("Enter your name:- ")

# try:
#     logging.info("started form....................!")
#     logging.info(NAME)
#     Emp1 = int(input("Enter your first numnber:- "))
#     Emp2 = int(input("Enter your second number:- "))
#     logging.info(f"Enter first value:- {Emp1}")
#     logging.info(f"Enter second value:- {Emp2}")
#     logging.info(f"return value:- {Emp1/Emp2}")
#     logging.info("ended..........!")
#     print(Emp1/Emp2)
    
# except Exception as msg:
#     logging.error(msg)

# -----------------------------------------------------


"""


import logging

LOGGER_DFILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


C_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOGGER_DFILE_PATH)

c_format = logging.Formatter("%(asctime)s---%(levelname)s---%(message)s")
f_format = logging.Formatter("%(asctime)s---%(process)i---[%(levelname)s]---%(message)s")


C_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(C_handler)
logger.addHandler(f_handler)



logger.debug("this is debugg")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")


"""

# ---------------------------------------------------------------------------------------

import logging


# LOGGER_FILR_PATH = r"python_logger/practise_user_defined.log"

# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


# rotating_handler = RotatingFileHandler(LOGGER_FILR_PATH)
# rotating_handler.setLevel(logging.DEBUG)


# format = logging.Formatter("%(asctime)s---%(filename)s---%(message)s")

# rotating_handler.setFormatter(format)

# logger.addHandler(rotating_handler)


# logger.debug("This is debugg")
# logger.info("This is info")
# logger.warning("This is warning")
# logger.error("This is error")
# logger.critical("This is critical")

# ------------------------------------------------------------------------------------------------------------

# import logging

# LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"

# from logging.handlers import RotatingFileHandler


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# rotating_handler = RotatingFileHandler(LOGGER_FILE_PATH, maxBytes=80, backupCount=5)
# rotating_handler.setLevel(logging.DEBUG)

# format = logging.Formatter("%(asctime)s---%(levelname)s---%(message)s")

# rotating_handler.setFormatter(format)

# logger.addHandler(rotating_handler)

# logger.debug("This is debug")
# logger.info("This is info")
# logger.warning("This is warning")
# logger.error("This is error")
# logger.critical("This is critical")

# -----------------------------------------------------------------------------------------------------------------

"""

import logging

LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"

from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


time_totating_handler = TimedRotatingFileHandler(LOGGER_FILE_PATH, when="s", interval= 2, backupCount=10)

format = logging.Formatter("%(asctime)s---%(levelname)s---%(message)s")

time_totating_handler.setFormatter(format)


logger.addHandler(time_totating_handler)

import time
a = time.time()
for i in range(1,10):
    logger.debug("This is debug")
    logger.info("This is info")
    logger.warning("This is warning")
    logger.error("This is error")
    logger.critical("This is critical")
    time.sleep(1)
b = time.time()
print(b-a)


"""

# ------------------------------------------------------------------------------------------------------------------------


LOGGER_FILE_PATH = r"F:\Python(Rohit)\python_logger\practise_log.log"
import logging

logging.basicConfig(format="%(asctime)s---%(levelname)s---%(message)s", 
                    filename= LOGGER_FILE_PATH, level = logging.DEBUG)



logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")

# for loop:-

for i in range(1,100):
    print(i,"Rohit gaikwad")



a = int(input("Enter your first nubmer:- "))
b = int(input("Enter your second nubmer:- "))
print(a+b)



print("hiii")