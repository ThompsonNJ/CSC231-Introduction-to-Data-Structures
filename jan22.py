class Patient:
    def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age

    def __str__(self):
        return self.name+', '+self.gender+', '+str(self.age)
    

class FamilyPatient(Patient):     
    def days_until_visit(self):
        if (self.gender.lower() == 'male' and self.age >= 45) or (self.gender.lower() == 'female' and self.age >= 55):
            return 180
        else:
            return 360

class CardioPatient(Patient):
    def days_until_visit(self):
        if self.age >= 65:
            return 90
        else:
            return 180

patients = []
cardio_patients = []

patient1 = FamilyPatient('Adam', 'Male', 1)
patients.append(patient1)
print(patient1)
print(patient1.days_until_visit())

patient2 = FamilyPatient('Eve', 'Female', 1)
patients.append(patient2)
print(patient2)
print(patient2.days_until_visit())

patient3 = FamilyPatient('Grandpa', 'Male', 100)
patients.append(patient3)
print(patient3)
print(patient3.days_until_visit())

patient4 = FamilyPatient('Grandma', 'Female', 100)
patients.append(patient3)
print(patient4)
print(patient4.days_until_visit())


x = FamilyPatient('Horace Butterworth', 'Male', 45)
print("Days until next visit:", x.days_until_visit())

x.age = 900
print(x.age)

cpatient1 = CardioPatient('Adam', 'Male', 65)
print(cpatient1)
print(cpatient1.days_until_visit())
