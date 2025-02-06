import argparse

'''
parser = argparse.ArgumentParser(description="The script will greet the user")
parser.add_argument("name",help="pass the user name")
args = parser.parse_args()

print(f"Hello, {args.name}")
'''
'''
#positional args
parser = argparse.ArgumentParser(description="Add two number")
parser.add_argument("num1",type=float, help="First number")
parser.add_argument("num2",type=float, help="Second number")

args = parser.parse_args()

print(f'Sum of two numbers: {args.num1 + args.num2}')
'''
'''
#Optional Args - Boolan Flags

parser = argparse.ArgumentParser(description="The script display useage of optional args")
parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

i=1
print("Hello")
while(i<10):
    if args.verbose:
        print("Verbose mode enabled")
    i+=1
print("World")
'''
'''
#Optional Args - Default Values

parser = argparse.ArgumentParser(description="The script display useage of optional args (default values)")

parser.add_argument("-r","--repeat", type=int,default=1, help="Number of repetitations")
args = parser.parse_args()
print(f'Repeating {args.repeat} times')
'''
parser = argparse.ArgumentParser(description="Additional Features argparse")

parser.add_argument(
    "--operation",
    choices=["add","sub","mul","div"],
    help="Operation to perform"
)
args = parser.parse_args()

print(args)




