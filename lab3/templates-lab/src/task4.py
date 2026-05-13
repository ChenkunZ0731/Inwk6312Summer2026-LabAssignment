from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task4.j2")

class NetworkInterface(object):
  def __init__(self,   description, vlan, ):
    self.description = description
    self.vlan = vlan
interface_obj = NetworkInterface("Server Port", 10)
print(template.render(interface=interface_obj))