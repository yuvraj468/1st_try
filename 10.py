class Car :
    def setenginemodel(self,engine):
        self.engine = engine

    def getenginemodel(self):
        print(self.engine)

class Honda(Car):
    def setcarmodel(self,model):
        self.model = model

    def getcarmodel(self):
        print(self.model)

mycar = Honda()

mycar.setenginemodel("EK-1")
mycar.setcarmodel("V6")
mycar.getenginemodel()
mycar.getcarmodel()