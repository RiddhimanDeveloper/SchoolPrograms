class Car: # this is the object
    def __init__(self, n, e):  #constructor, self is not a parameter, n and e are parameters
         self.__VehicleID = n
         self.__Registration = ""      # two underscores to indicate that attribute is private. the attributes cant be used outside the class
         # (__Registration is an attribute for example)
         self.__DateOfRegistration = None
         self.__EngineSize = e
         self.__PurchasePrice = 0.00

    def SetPurchasePrice(self,p): # this is called a method (subroutine) (methods are usually public for accessibility outside the class)
        self.__PurchasePrice = p

    def SetRegistration(self,r):
        self.__Registration = r

    def SetDateOfRegistration(self,d):
        self.__DateOfRegistration = d

    def GetVehicleID (self):
        return(self.__VehicleID)

    def GetRegistration(self):
        return(self.__Registration)

    def GetDateOfRegistration(self):
        return(self.__DateOfRegistration)

    def GetEngineSize(self):
        return(self.__EngineSize)

    def GetPurchasePrice(self):
        return(self.__PurchasePrice)

def printAll():
    print()

# Task starts here
maxprice = 0
maxpricemodel = ""
maxengine = 0
maxenginemodel = ""
total = 0


for i in range(0,5):
    Model = input("Enter name of the Toyota car model: ")
    ID = int(input("Enter CarID: "))
    Registration = int(input("Enter registration number: "))
    DOR = input("Enter Date of Registration: ")
    EngSize = int(input("Enter engine size: "))
    PurchasePrice = int(input("Enter purchase price of model: "))

    total += PurchasePrice
    if PurchasePrice > maxprice:
        maxprice = PurchasePrice
        maxpricemodel = Model

    if EngSize > maxengine:
        maxengine = EngSize
        maxenginemodel = Model

    Model = Car(ID, EngSize)
    Model.SetRegistration(Registration)
    Model.SetDateOfRegistration(DOR)
    Model.SetPurchasePrice(PurchasePrice)

    print("ID: ", Model.GetVehicleID())
    print("EngineSize: ", Model.GetEngineSize())
    print("Registration: ", Model.GetRegistration())
    print("Date of Registration: ", Model.GetDateOfRegistration())
    print("Purchase price : ", Model.GetPurchasePrice())


avg = total/5
print("Average purchase price of all cars is:", avg)
print("Car with highest purchase price is: ", maxpricemodel, "with a price of ", "$", maxprice)
print("Car with largest engine size is: ", maxenginemodel, "with a size of ", maxengine)

carjobs1=[Car("",0) for i in range(5)]
carjobs2=[]
for i in range(2):
    carattr1=input("Please enter the veichle ID ")
    carattr2=input("Please enter the engine size")
    carjobs2.append(Car(carattr1,carattr2))
for i in range (len(carjobs1)):
    print("Please enter the Purchase Price for",carjobs1[i].GetVehicleID())
    pprice=input()
    carjobs1[i].SetPurchasePrice(pprice)
    print("Please enter the registration for ", carjobs1[i].GetVehicleID())
    RegNo=input()
    carjobs1[i].SetRegistration(RegNo)
    print("Please enter the Date of Reg for ", carjobs1[i].GetVehicleID())
    date=input()
    carjobs1[i].SetDateOfRegistration(date)
for i in range(len(carjobs1)):
    print("Veichle ID",carjobs1[i].GetVehicleID())
    print("Reg No",carjobs1[i].GetRegistration())
    print("DateOfRegistration",carjobs1[i].GetDateOfRegistration())
    print("Engine Size", carjobs1[i].GetEngineSize())
    print("Purchase Price",carjobs1[i].GetPurchasePrice())

carToDisplay=input("please enter Veichle ID of car to view the details:\n")
for i in range(len(carjobs2)):
    if carToDisplay==carjobs2[i].GetVehicleID():
        print("Veichle ID", carjobs2[i].GetVehicleID())
        print("Reg No", carjobs2[i].GetRegistration())
        print("DateOfRegistration", carjobs2[i].GetDateOfRegistration())
        print("Engine Size", carjobs2[i].GetEngineSize())
        print("Purchase Price", carjobs2[i].GetPurchasePrice())


