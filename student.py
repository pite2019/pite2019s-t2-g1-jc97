class Student:

    ABSENT = -1

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__scores = []


    def add_score(self, class_name, date, score):
        if isinstance(score, int) and score >= Student.ABSENT:
            self.__scores.append([class_name, date, score])
        else:
            raise ValueError(int)


    def average_in_class(self, class_name, ignore_absent=False):
        sum = 0
        count = 0
        for l in self.__scores:
            if l[0] == class_name:
                if l[2] == Student.ABSENT:
                    if ignore_absent == False:
                        count += 1
                else:
                    sum += l[2]
                    count += 1
        average = sum / count
        return average


    def get_class_list(self):
        classes = []
        for l in self.__scores:
            if not l[0] in classes:
                classes.append(l[0])
        return classes


    def average_all_classes(self, ignore_absent=False):
        classes = self.get_class_list()
        sum = 0
        count = len(classes)
        for c in classes:
            sum += self.average_in_class(c, ignore_absent)
        average = sum/count
        return average
