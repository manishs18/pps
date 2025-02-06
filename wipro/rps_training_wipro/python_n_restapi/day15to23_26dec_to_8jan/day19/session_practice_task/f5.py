import json


'''
d1 = {'Name':'Manish','Age':25,'Gender':'M'}

with open("data.json","w") as fp:
    json.dump(d1,fp)
'''

# with open("data1.json","r") as fp:
#     content = json.load(fp)
#
#
# print(type(content))
# print(content)


d1 = {
    'Name':
          {
              'fName':'Manish',
              'sName':'Singh'
          },
    'Address':
        {
            'line1':'abcd1',
            'line2':'abcd2',
            'pincode':560079
        }
      }
with open("data2.json","w") as fp:
    json.dump(d1,fp)