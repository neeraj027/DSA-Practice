class Animal:
    animal_type='mammal'
    def __init__(self,name,age):
        self.__name=name
        self.age=age
        
dog1=Animal('luna',5)
dog1.name='pug'
print(dog1.name)