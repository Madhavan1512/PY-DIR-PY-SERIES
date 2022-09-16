class Human:
    def __init__(self, name , occupation):
        self.name = name
        self.occupation = occupation
        
    def do_work(self):
        if self.occupation == 'Tennis Player':
            print(self.name , "plays tennis")   
        elif self.occupation == 'Actor':                   
            print(self.name , "shoots a film")  
    def speaks(self):
        print(self.name , "says how are you?") 
        
tom = Human('Tom Cruise','Actor')
tom.do_work()
tom.speaks()