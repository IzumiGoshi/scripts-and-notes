from jinja2 import Template
with open('template.html.jinja2') as file_:
    template = Template(file_.read())
template.render(name='John')
