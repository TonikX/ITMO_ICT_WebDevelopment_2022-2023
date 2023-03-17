class marks_dao:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.marks = dict()
        self.fill_dict()

    def fill_dict(self):
        file = open(self.path_to_data,"r")
        text = file.read().split("\n")
        if "" in text: text.remove("")
        if len(text) == 0:
            print("Src file is empty. No info about marks")
            return
        for line in text:
            row = list()
            line = line.split(": ")
            subject, marks = line
            marks = marks.split()
            if "" in marks: marks.remove("")
            for mark in marks:
                row.append(int(mark))
            self.marks[subject] = row
        print("Dictionary filled")
        file.close()

    def add(self, subject, mark):
        if subject not in self.marks.keys():
            self.marks[subject] = list()
        self.marks[subject].append(int(mark))
        self.update_file()

    def update_file(self):
        file = open(self.path_to_data, "w")
        for key in self.marks:
            file.write("%s: "%(key))
            for mark in self.marks[key]:
                file.write("%d "%(mark))
            file.write("\n")
        file.flush()
        file.close()
    
    def get_marks(self):
        return self.marks
    
    def get_marks_subject(self, subject):
        if subject not in self.marks.keys():
            raise Exception("not found")
        return self.marks[subject]