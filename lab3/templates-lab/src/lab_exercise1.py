from jinja2 import Environment, FileSystemLoader
import yaml
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-labexercise1.j2")

with open("lab_exercise1.yml") as f:
  data = yaml.load(f, Loader=yaml.SafeLoader)
  print(template.render(routers=data["routers"]))