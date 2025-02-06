import sys

print(f'number of args passed as CLI = {len(sys.argv)}')
print(f'arg list is, {sys.argv}')

for i in sys.argv:
    print(i)
