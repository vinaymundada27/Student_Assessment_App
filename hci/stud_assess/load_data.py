from .models import Student
from adaptor.model import CsvDbModel


class MyCsv(CsvDbModel):
    class Meta:
        dbModel = Student
        delimiter = ","


filename = "data.csv"
my_csv_list = MyCsv(data=open(filename))