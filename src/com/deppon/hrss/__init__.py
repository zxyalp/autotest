import logging
import os
import sys
import unittest
import pprint
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support import expected_conditions as ex
from time import sleep,strftime
from datetime import datetime
 
from .publ.log4 import Logger
from .publ.log4 import log
from .func.login import startup,menu,login
from com.deppon.hrss.publ.categories import categories
from .publ.data import data
from .publ.calendar import calendar
import globalvar.globalvar

