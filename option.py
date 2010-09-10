import re

class Option:
    def __init__(self):
        self.i=0    #ignore case
        self.m=0    #multiline
        self.s=0    #dot all
        self.u=0 #unicode, default on
        self.x=0    #verbose
        self.lang=""    #language, default python
        self.action=0  #action: 1:match, 2:replace, 3:split
        

    def get_flags(self):
        return self.i | self.m | self.s | self.u | self.x
    
    def __str__(self):
        return "lang: %s; flags: %d; tab: %s;" % (self.lang, self.get_flags(),
                                                  ("Match", "Replace", "Split")[self.action])
    def __repr__(self):
        return self.__str__()
        
    def set(self, name, value):
        
        if  name in ('i', 'm', 's', 'x', 'u'):
            value=str(value).lower()
            if value=='true':
                self.__dict__[name] = re.__dict__[name.upper()]
            else:
                self.__dict__[name] = 0
        elif name == 'action':
            self.action = int(value)
        elif name == 'lang':
            print "before", self.lang
            self.lang = value
            print "after", self.lang

