class WaitingRoom:
    def __init__(self):
        self.patients = []

    def add(self, name):
        self.patients.append(name)

    def is_empty(self):
        if len(self.patients) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.patients)
        
    def display(self):
        count = 1
        for i in self.patients:
            print("{} {}".format(count, i))
            count += 1
            
    def read_from_file(self, filename):
        count = 0
        with open(filename, 'r') as file:
            patient_list = file.readlines()
            for i in patient_list:
                patient_list[count] = i.strip()
                count += 1
                
            self.patients = patient_list

    def remove(self, name):
        if name in self.patients:
            return self.patients.remove(name)
        else:
            return None
    

##    def position(self, name):
##        count = 1
##        for i in self.patients:
##            count += 1
##
##        return self.patients[name]
            

        
