class Vehicle():
    def __init__(self,company,model,color,engine,fuel):
        self.veh_company=company
        self.veh_model=model
        self.veh_color=color
        self.veh_engine=engine
        self.veh_fuel=fuel
    
    def Car_start(self):
        print('vrooom vrooom vrooooom')
    
    def Change_gear(self):
        print('stutututututut stuuututu')
           
class Car(Vehicle):
    def __init__(self, company, model, color, engine, fuel,body_type):
        super().__init__(company, model, color, engine, fuel)
        self.body_type=body_type
    def  open_Sunroof(self):
        print('sunroof opening')       
        
        
car1=Car('bmw','m5','black','v8','petrol','suv')
print(car1.veh_company)
car1.Car_start()
car1.Change_gear()
car1.open_Sunroof()