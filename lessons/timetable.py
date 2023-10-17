from __future__ import annotations
import csv
class File:
    def __init__(self, path: str):
        self.path = path
    def load(self):
        with open(self.path, "r", newline='' ) as file:
            return list(csv.reader(file))
    def write(self, val: list[list]):
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            for line in val:
                writer.writerow(line)

class Timetable:
    LESSON_LENGTH = 3
    def __init__(self, filepath: str=r"timetable.txt"):
        self.table = [["===" for i in range(6)] for e in range(5)]
        self.file_handler = File(filepath)
    def menu(self):
        choice = 0
        while choice != 5:
            choice = input("""
1. Output timetable

2. Edit a lesson

3. Load

4. Save

5. Close""")
            match choice:
                case '1':
                    print(str(self))
                case '2':
                    print(self.edit())
                case '3':
                    self.load()
                case '4':
                    self.save()
    def __access(self, day, lesson):
        return self.table[lesson - 1][day - 1]
    def __modify(self, day, lesson, val):
        self.table[lesson - 1][day - 1] = val
    def edit(self):
        day = input("enter day")
        lesson = input("enter lesson")
        self.__modify(int(day), int(lesson), (lambda x: x[:Timetable.LESSON_LENGTH].upper() if len(x) >= Timetable.LESSON_LENGTH else x.ljust(Timetable.LESSON_LENGTH).upper())(input()))
        return "Lesson updated."
    def load(self):
        self.table = self.file_handler.load()
    def save(self):
        self.file_handler.write(self.table)
    def __str__(self) -> str:
        return f" |-{'-||-'.join(str(i) for i in range(1, 1 + len(self.table[0])))}-|" + ''.join(f"\n{i}|{'||'.join(self.table[i - 1])}|" for i in range(1, 1 + len(self.table)))
Timetable().menu()

