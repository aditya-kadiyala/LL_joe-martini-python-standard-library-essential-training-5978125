# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
parser = configparser.ConfigParser()

# TODO: Read the configuration file
parser.read("config.cfg")

# TODO: print the sections
# print(parser.sections())
# print(parser.has_section("Section 1"))
# print(parser.has_section("Section 31"))

# TODO: Access one of the default values
# using_time_travel = parser['DEFAULT']['UseTimeTravel']
# print(type(using_time_travel))
# print(using_time_travel)

# ustb = bool(using_time_travel)
# print(type(ustb))
# print(ustb)

# TODO: Demonstrate the getXXX convenience functions
obd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(obd)

speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)
# TODO: Access a non-existent value
maxspeed = parser['DEFAULT'].getfloat('MAXShipSpeed')
if maxspeed is None:
  print("ShipSpeed is ")

try:
  maxspeeddefault = parser['DEFAULT']['MAXSpeed']
  print(maxspeeddefault)
except KeyError as e:
  print("There is no", e)
