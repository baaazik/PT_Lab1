# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from CalcGoodCount import CalcGoodCount
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    count = CalcGoodCount(students).calc()
    print("Хорошисты: ", count)


if __name__ == "__main__":
    main()
