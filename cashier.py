"""
File: cashier.py
"""

from queue import LinkedQueue

class Cashier(object):

    def __init__(self,num):
        self._totalCustomerWaitTime = 0
        self._customersServed = 0
        self._currentCustomer = None
        self._queue = LinkedQueue()
        self._number = num

    def addCustomer(self, c):
        self._queue.enqueue(c)

    def getNum(self):
        return self._number
   
    def serveCustomers(self, currentTime):
        if self._currentCustomer is None:
            # No customers yet
            if self._queue.isEmpty():
                return
            else:
                # Dequeue first waiting customer and tally results
                self._currentCustomer = self._queue.dequeue()
                self._totalCustomerWaitTime += \
                                            currentTime - \
                                            self._currentCustomer.arrivalTime()
                self._customersServed += 1

        # Give a unit of service
        self._currentCustomer.serve()

        # If current customer is finished, send it away   
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None
   
    def __str__(self):
        result = "TOTALS FOR THE CASHIER " + str(self.getNum()) + "\n" +\
                 "Number of customers served:        " + \
                 str(self._customersServed) + "\n"
        if self._customersServed != 0:
            aveWaitTime = float(self._totalCustomerWaitTime) /\
                          self._customersServed
            result += "Number of customers left in queue: " + \
                      str(len(self._queue)) + "\n" + \
                      "Average time customers spend\n" + \
                      "waiting to be served:              " + \
                      "%5.2f" % aveWaitTime
        return result
