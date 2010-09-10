#!/usr/bin/python
import web
import re
from jinja2 import Environment, PackageLoader
from option import Option
from textarea import TextArea

urls = ("/", "index",
        "/option",'options',
        "/text", "textarea",
        
        )
reoptions = [
            ('s', 'dotall', 'Dot Match All'),
            ('i', 'ignorecase', 'Case Insensitive'),
            ('m', 'multiline', '^$ at line breaks'),
            ('x','verbose','Free-Spacing'),
            ('u', 'unicode', 'Unicode')
        ]

funcs = [
        '',
    'Import regex library',
    'If/else branch whether the regex matches (part of) a string'
    ]

langs= ('python',)
app = web.application(urls, globals())
flag = Option()
text = TextArea()
env  = Environment(loader=PackageLoader('index', 'templates'))

#the home page(the only page)
class index:
    def GET(self):
        template = env.get_template('index.html')
        return template.render(reoptions=reoptions,
                               functions=funcs,
                               langs=langs
                               )
        
#when option changes in the front, 
class options:
    def POST(self):
        global flag
        i=web.input()
        try:
            flag.set(i.name,i.value)
        except:
            raise ValueError

class textarea:
    def POST(self):
        global flag
        global text
        i=web.input()
        try:
            text.set(i.name, i.value)
            text.do(flag)
            return text.get()
        except:
            raise 'error happened'
if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
