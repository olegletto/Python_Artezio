class Student(object):

    def __init__(self, name, conf):
        self.name = name
        self.__dict__.update(conf)
        """
        conf = {'exam_max':'30', 'lab_max':'7', 'lab_num':'10', 'k':'0.61'}

        """


    def make_lab (self, m, n=1):
        """m = float lab_max, n = int 0...lab_num-1"""

        return self

