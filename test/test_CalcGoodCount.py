from src.Types import DataType
from CalcGoodCount import CalcGoodCount
import pytest



class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        good_students_count = 1

        return data, good_students_count

    def test_init_calc_rating(
            self,
            input_data: tuple[DataType, int]) -> None:
        calc_rating = CalcGoodCount(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self,
                  input_data: tuple[DataType, int]) -> None:
        count = CalcGoodCount(input_data[0]).calc()
        assert count == input_data[1]