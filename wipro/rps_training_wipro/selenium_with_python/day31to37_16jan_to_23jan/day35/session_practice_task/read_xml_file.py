import xml.etree.ElementTree as ET

#load the xml file and parse the file
tree = ET.parse(r"C:\Users\mkuma\OneDrive\Desktop\my_repo\ManishDTA\selenium_with_python\day31to37_16jan_to_23jan\day35\session_practice_task\data.xml")
root = tree.getroot()

#success the root tag

print(f"The root tag is: {root.tag}")

for employee in root.findall('employee'):
    emp_id = employee.find('id').text
    name = employee.find('name').text
    department = employee.find('department').text
    address = employee.find('Address').text
    print(f"ID: {emp_id}, Name: {name}, Department: {department}, Address: {address}")
