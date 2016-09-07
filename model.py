"""
File: model.py
"""

from cashier import Cashier
from customer import Customer

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numberOfLines):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._numberOfLines = numberOfLines
        self._cashiers = [] # create a list of that contains many cashiers
        for i in xrange(numberOfLines):
            cashier = Cashier(i)
            self._cashiers.append(cashier)
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in xrange(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus,self._numberOfLines)

            # Send customer to cashier if successfully generated
            if customer != None:
                customerLine = customer.getLine()
                optCashier = self._cashiers[customerLine]
                for cashier in self._cashiers:
                    if abs(customerLine - cashier.getNum()) <= 3: #no more than three lines away.
                        minQueue = len(optCashier._queue)
                        if minQueue > len(cashier._queue):
                            optCashier = cashier     
                optCashier.addCustomer(customer)

            # Tell each cashier to provide another unit of service
            for cashier in self._cashiers:
                cashier.serveCustomers(currentTime)
        result = ''        
        for cashier in self._cashiers:
            result += str(cashier) + "\n"

        return result 
            
        
