from jinja2 import Environment, FileSystemLoader
import yaml
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-labexercise2.j2")

with open("lab_exercise2.yml") as f:
  data = yaml.load(f, Loader=yaml.SafeLoader)
  print(template.render(routers=data["routers"]))