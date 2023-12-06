# -*- coding: utf-8 -*-
from Types import DataType

class CalcGoodCount:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count = 0

    def calc(self) -> int:
        good_count = 0

        for key in self.data:
            is_student_good = True

            for subject in self.data[key]:
                if subject[1] < 76:
                    is_student_good = False

            if is_student_good:
                good_count += 1

        self.count = good_count
        return self.count
