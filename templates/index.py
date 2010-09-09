#!/usr/bin/python
import web
import re
from option import Option
from jinja2 import Environment, PackageLoader

urls = ("/", "index",
        "/option.*",'REoption', 
        )
reoptions = [
            ('s', 'dotall', 'Dot Match All'),
            ('i', 'ignorecase', 'Case Insensitive'),
            ('m', 'multiline', '^$ at line breaks'),
            ('x','verbose','Free-Spacing'),
        ]

funcs = [
        '',
    'Import regex library',
    'If/else branch whether the regex matches (part of) a string'
    ]
app = web.application(urls, globals())

flag = Option()
env  = Environment(loader=PackageLoader('index', 'templates'))

class index:
    def GET(self):
        template = env.get_template('index.html')
        return template.render(reoptions=reoptions, functions=funcs)

class REoption:
    def POST(self):
        global flag
        i=web.input()
        try:
            flag.set(i.name,i.value) 
        except:
            raise ValueError

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
