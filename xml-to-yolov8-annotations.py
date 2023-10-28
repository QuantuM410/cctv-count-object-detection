import os
import xml.etree.ElementTree as ET

# Define your label mapping
label_map = {"vehicle": 0, "construction": 1,
             "bus": 2, "cyclist": 3, "pedestrian": 4}

# Directory containing XML annotations
xml_dir = "Annotations/"

# Directory to save YOLOv8 format text files
output_dir = "yolo-labels/"

# Function to convert XML annotation to YOLOv8 format


def convert_xml_to_yolo(xml_path, output_dir):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    image_filename = root.find("filename").text
    yolo_filename = os.path.splitext(image_filename)[0] + ".txt"

    with open(os.path.join(output_dir, yolo_filename), "w") as yolo_file:
        for obj in root.findall("object"):
            class_name = obj.find("name").text
            if class_name in label_map:
                class_id = label_map[class_name]
                bbox = obj.find("bndbox")
                width = int(root.find("size/width").text)
                height = int(root.find("size/height").text)
                x_center = (float(bbox.find("xmin").text) +
                            float(bbox.find("xmax").text)) / 2.0 / width
                y_center = (float(bbox.find("ymin").text) +
                            float(bbox.find("ymax").text)) / 2.0 / height
                box_width = (float(bbox.find("xmax").text) -
                             float(bbox.find("xmin").text)) / width
                box_height = (float(bbox.find("ymax").text) -
                              float(bbox.find("ymin").text)) / height

                yolo_file.write(
                    f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


# Iterate through XML files and convert to YOLOv8 format
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_dir, xml_file)
        convert_xml_to_yolo(xml_path, output_dir)
