import xml.etree.ElementTree as ET

#load the xml file and parse the file
tree = ET.parse(r"C:\Users\mkuma\OneDrive\Desktop\my_repo\ManishDTA\selenium_with_python\day31to37_16jan_to_23jan\day35\lab_session\data1.xml")
root = tree.getroot()

#success the root tag

print(f"THe root tag is {root.tag}")

for emp in root.findall('book'):
    title = emp.find('title').text
    print(title)
