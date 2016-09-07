"""
File: customer.py
"""

import random

class Customer(object):

    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime,
                         averageTimePerCustomer, numberOfLines):
        """Returns a Customer object if the probability 
        of arrival is greater than or equal to a random number.
        Otherwise, returns None, indicating no new customer.
        """                                     
        if random.random() <= probabilityOfNewArrival:
            timePerCustomer = random.randint(1, 2 * averageTimePerCustomer + 1)
            line = random.randint(0, numberOfLines-1)
            return Customer(arrivalTime, timePerCustomer,line)
        else:
            return None
       
    def __init__(self, arrivalTime, serviceNeeded, line):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded
        self._line = line

    def arrivalTime(self):
        return self._arrivalTime

    def getLine(self):
        return self._line   
   
    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded
   
    def serve(self):
        """Accepts a unit of service from the cashier."""
        self._amountOfServiceNeeded -= 1
