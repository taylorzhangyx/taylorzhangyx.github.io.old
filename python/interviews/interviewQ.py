# There's a Stark café opening in your school and you are invited to create
# an ordering system for the coffee shop.
# However you don't have money to pay for
# a cloud computing instance so you must use the API they provide you to store the orders.

# # They have the following strange storage API:
# storageNo1.push(orderNumber)
# storageNo1.pop()
# storageNo2.push(orderNumber)
# storageNo2.pop()

# # In these APIs your order which comes in first are return last. For ex,
# storageNo1.push(1);
# storageNo1.push(2);
# storageNo1.pop(); // returns 2;
# storageNo1.pop(); // returns 1;

# # storageNo1 & storageNo2 are essentially the same.
# # And you need to use the above data structure to
# # create a ordering service in which orders comes first are returned first. For ex,
# yourService.addOrder(1);
# yourService.addOrder(2);
# yourService.addOrder(3);
# yourService.getOrder(); // outputs 1
# yourService.getOrder(); // outputs 2
# yourService.getOrder(); // outputs 3


class MyService:
    def __init__(self, storage1, storage2):
        self.storageAdd = storage1
        self.storageGet = storage2
        self.size = 0
        self.getSize = 0
        self.addSize = 0

    # when storageGet is empty, we need to transfer the storageAdd into storageGet to fix the order
    def _balanceStorage(self):
        countToMove = self.addSize
        for i in range(countToMove):
            order = self.storageAdd.pop()
            self.addSize -= 1
            self.storageGet.push(order)
            self.getSize += 1

    def addOrder(self, orderNumber):
        self.storageAdd.push(orderNumber)
        self.addSize += 1

    def getOrder(self):
        # storageGet still have orders to pop
        if self.getSize > 0:
            self.getSize -= 1
            return self.storageGet.pop()
        # No orders in the storage
        elif self.getSize == 0 and self.addSize == 0:
            raise Exception("No order exist!")
        # storageGet is empty, balance the storageAdd to storageGet to fix the order
        elif self.getSize == 0 and self.addSize > 0:
            self._balanceStorage()
            return self.getOrder()


class storageMock:
    def __init__(self):
        self.store = []

    def push(self, data):
        self.store.append(data)

    def pop(self):
        return self.store.pop()


# Simple tests
myserViceTest = MyService(storageMock(), storageMock())
myserViceTest.addOrder(1)
myserViceTest.addOrder(2)
myserViceTest.addOrder(3)
print(myserViceTest.getOrder()) # 1
print(myserViceTest.getOrder()) # 2
myserViceTest.addOrder(4)
myserViceTest.addOrder(5)
myserViceTest.addOrder(6)
myserViceTest.addOrder(7)
myserViceTest.addOrder(8)
print(myserViceTest.getOrder()) # 3
print(myserViceTest.getOrder()) # 4
print(myserViceTest.getOrder()) # 5
myserViceTest.addOrder(9)
print(myserViceTest.getOrder()) # 6
print(myserViceTest.getOrder()) # 7
print(myserViceTest.getOrder()) # 8
