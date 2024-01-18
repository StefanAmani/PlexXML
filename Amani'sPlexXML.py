import os
import xml.etree.ElementTree as ET

# Create the file structure
movie = ET.Element('movie')

# Ask the user for input and create the XML elements
title_text = input("Please enter the movie title: ")
title_year = input("Please enter the movie year: ")
title = ET.SubElement(movie, 'title')
title.text = f"{title_text} ({title_year})"

releasedate = ET.SubElement(movie, 'releasedate')
releasedate.text = input("Please enter the release date (YYYY-MM-DD): ")

# Loop to add multiple actors
while True:
    actor = ET.SubElement(movie, 'actor')

    name = ET.SubElement(actor, 'name')
    name.text = input("Please enter the actor's name: ")

    role = ET.SubElement(actor, 'role')
    role.text = input("Please enter the actor's role: ")

    thumb = ET.SubElement(actor, 'thumb')
    thumb.text = input("Please enter the actor's thumbnail URL (must be an Imgur address): ")

    add_another = input("Would you like to add another actor? (yes/no): ")
    if add_another.lower() != 'yes':
        break

# Create the XML file
tree = ET.ElementTree(movie)

# Find the path to the desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Save the XML file to the desktop with the title provided by the user
filename = f"{title_text} ({title_year}).xml"
tree.write(os.path.join(desktop, filename))
