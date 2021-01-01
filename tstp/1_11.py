class rec():
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def area(self):
        return self.width * self.len
    
        
    def rot(self,w,l):
        self.width = w
        self.len = l
        return self.width/self.len
rec = rec(10,20)
rec.rot(20,40)
print(rec.area())
print(rec.rot(20,40))
