import re

class Option:
    def __init__(self):
        self.i=0    #ignore case
        self.m=0    #multiline
        self.s=0    #dot all
        self.u=re.U #unicode, default on
        self.x=0    #verbose

    def get(self):
        return self.i | self.m | self.s | self.u | self.x 

    def set(self, name, value):
        flag=name.lower()
        value=str(value).lower()
        if value=='true' and flag in ('i', 'm', 's', 'x'):
            self.__dict__[flag]=re.__dict__[flag.upper()]
        else:
            self.__dict__[flag]=0


