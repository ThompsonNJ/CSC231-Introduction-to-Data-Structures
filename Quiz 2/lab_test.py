class LabTest:

    def __init__(self, name, priority, procedure):
        self.name = name
        self.priority = int(priority)
        self.procedure = procedure

    def __str__(self):
        return "{} {} {}".format(str(self.name), str(self.priority), str(self.procedure))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(other) is type(self):
            return self.name == other.name and self.priority == other.priority and self.procedure == other.procedure
        else:
            return False
