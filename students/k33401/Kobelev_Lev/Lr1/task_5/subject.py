class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_mark(self, mark):
        self.marks.append(mark)
