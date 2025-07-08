#Class is the template
#Object is something workable we create using a class as template

# class Employee:
#     company = "HP"

#     def salary(self):
#         return 34000
    
# em = Employee()
# print(em.salary())

class car:
    company = "BMW"
    model = "M5"

    def color(self):
        return "black"
    
c = car()
print(c.color())
print(c.company)
print (c.model)
print(c.color(), c.company, c.model)