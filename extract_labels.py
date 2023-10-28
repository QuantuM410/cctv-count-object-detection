import os
import xml.etree.ElementTree as ET

label_set = set()  # Create an empty set to store unique labels

# Directory containing XML annotations
xml_dir = "Annotations/"

# Iterate through XML files to extract labels
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_dir, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for obj in root.findall("object"):
            class_name = obj.find("name").text
            label_set.add(class_name)
            print(class_name)

# Convert the set of labels to a list
unique_labels = list(label_set)

# Print the list of unique labels
print(unique_labels)
