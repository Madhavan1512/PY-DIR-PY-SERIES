class Father :
    def gardening(self):
        print("I enjoy gardening")

class Mother :
    def cooking(self):
        print("I enjoy cooking")



class Child(Mother, Father):
    def sports(self):
        print("I enjoy sports")
        
c = Child()
c.cooking()
c.gardening()
c.sports()
