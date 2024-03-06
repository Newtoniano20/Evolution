from .model import *

class Chill(Model):
    def __repr__(self) -> str:
        return "Chill"
    def run(self, prev=None):
        return self.COLLABORATE

class Attacker(Model):
    def __repr__(self) -> str:
        return "Attacker"
    def run(self, prev=None):
        return self.ATTACK

class Repeater(Model):
    def __repr__(self) -> str:
        return "Repeater"
    def run(self, prev=None):
        if prev == None:
            return self.COLLABORATE
        return prev
    
class Jumper(Model):
    def __init__(self):
        super().__init__()
        self.previously = None
    
    def __repr__(self) -> str:
        return "Jumper"

    def run(self, prev=None):
        if self.previously == None or self.previously == self.ATTACK:
            self.previously = self.COLLABORATE
            return self.COLLABORATE
        else:
            self.previously = self.ATTACK
            return self.ATTACK

class Punisher(Model):
    def __init__(self):
        super().__init__()
        self.previously = False
    
    def prerun(self):
        self.previously = False

    def __repr__(self) -> str:
        return "Punisher"

    def run(self, prev=None):
        if prev == self.ATTACK or self.previously == True:
            self.previously = True
            return self.ATTACK
        else:
            return self.COLLABORATE
