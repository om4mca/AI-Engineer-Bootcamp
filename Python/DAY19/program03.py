#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Function Logger
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

import logging

# Configure to show all messages at or above INFO level
logging.basicConfig(level=logging.INFO)

# Logger functions by level
logging.debug("This won't print because level is INFO")
logging.info("Application successfully initialized.")
logging.warning("Low disk space warning.")
