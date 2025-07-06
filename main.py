# (No content at all)
# Implement auto diff engine here

class val:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"Value(data={self.data})"
        
    def __add__(self, other):
        return val(self.data + other.data)
    
    def __mul__(self, other):
        return val(self.data * other.data)
    
a = val(2)
b = val(-5)
print(a*b)