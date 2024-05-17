class employee :
   
   def __init__(self, id, name):
            self.id = id
            self.name = name


emp = employee(1, "coder")           
print(emp)
del emp.id
del emp
print(emp)