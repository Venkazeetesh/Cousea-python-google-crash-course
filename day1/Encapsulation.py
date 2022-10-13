class Mobile:
    def function(self,Mobile,Model,size):
        self.Mobile=Mobile
        self.Model=Model
        self.size=size
    def call(self,Mobile):
        print("calling to ",str(Mobile))
        
    def no(self):
        print(self.Mobile)
obj=Mobile("hi",)
obj.call="no"
print(obj.no)