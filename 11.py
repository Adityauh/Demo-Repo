class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
     # adding two objects 
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
  
    def __str__(self):
        return self.a, self.b
  
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
