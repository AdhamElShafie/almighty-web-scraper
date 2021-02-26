# import abc
# from abc import ABC, abstractmethod
import os
print(os.getcwd())

from selenium_client import SeleniumClient


class TestImplementABC(SeleniumClient):
    SOURCE_URL = 'https://www.amazon.ca'


print(TestImplementABC().SOURCE_URL)
print(TestImplementABC().DRIVER_PATH)
