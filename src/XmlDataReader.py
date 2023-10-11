# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        document = ET.parse(path)
        root = document.getroot()
        for elem in root.iter():
            print(elem.tag)
        return self.students