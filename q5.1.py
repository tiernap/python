import platform
import os

print("The machine type is {}".format(platform.machine()))
print("The machine hostname is {}".format(platform.node()))
print("The machine OS is {}".format(platform.system()))
print("The system PATH is {}".format(os.environ['PATH']))