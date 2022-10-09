#Here there is the feast in the jungle which the animals brings dishes to the place in which there is a condition that each animals 
#should bring at least one dishes in which the dishes name start and end with the animals name and write if or else statement in which 
#The animals are allowed to bring the lunch by returning True or False 

def feast(self,animal,dish):
    self.animal=animal 
    self.dish=dish
animal=['lion','tiger','zebra']
dish=['maango','apple','grape','onion']
for x in animal:
    for y in dish:
        animal[x[0]]=dish[y[0]]
        print("Allowed")