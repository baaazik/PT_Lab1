# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Парсим XML
        document = ET.parse(path)
        root = document.getroot()

        # Проходим по всем студентам в файле
        for root_child in root:
            if root_child.tag == "student":
                student_name = root_child.attrib["name"]
                subjects = []

                # Проходим по всем предметам в студенте
                for student_child in root_child:
                    if student_child.tag == "subject":
                        subject_name = student_child.attrib["name"]
                        mark = int(student_child.attrib["mark"])
                        subjects.append((subject_name, mark))

                self.students[student_name] = subjects
        return self.students
