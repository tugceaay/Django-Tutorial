from django.db import models
GRADE_CHOICES = (("PRI","İlkokul"),("MID","Ortaokul"),("HIGH","Lise"),("UNI","Üniversite"))
class SchoolModel(models.Model):
    #Okulun ismi, adresi, türü
    name = models.CharField(max_length=100, default="İsimsiz Okul")
    address = models.CharField(max_length=400, default="Adres yok")
    grade = models.CharField(max_length=4, default="PRI",choices=GRADE_CHOICES)

    def __str__(self):
        return "[" + self.grade + "]" + self.name + " - " + self.address

class ClassModel(models.Model):
    name = models.CharField(max_length=10, default="Belirsiz")
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.school.name + " - " + self.name

class StudentModel(models.Model):
    #isim, numara
    name = models.CharField(max_length=100, default="İsimsiz")
    number = models.CharField(max_length=10, default="Numarasız")
    classname = models.ForeignKey(ClassModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.classname.school.name.upper() + ": " + self.classname.name + " - " + self.name + " ({})".format(self.number)


class ParentModel(models.Model):
    name = models.CharField(max_length=100, default="İsimsiz")
    telno = models.CharField(max_length=100, default="Numara eklenmemiş.")
    childname = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " [{}] ".format(self.childname)
