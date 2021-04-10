from django.db import models

GRADE_CHOICES = (("PRI", "İlkokul"), ("MID", "Ortaokul"), ("HIGH", "Lise"), ("UNI", "Üniversite"))


class SchoolModel(models.Model):
    # Okulun ismi, adresi, türü
    name = models.CharField(max_length=100, default="İsimsiz Okul")
    address = models.CharField(max_length=400, default="Adres yok")
    grade = models.CharField(max_length=4, default="PRI", choices=GRADE_CHOICES)

    def __str__(self):
        return "[" + self.grade + "]" + self.name + " - " + self.address


class ClassModel(models.Model):
    name = models.CharField(max_length=10, default="Belirsiz")
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.school.name + " - " + self.name


class StudentModel(models.Model):
    # isim, numara
    name = models.CharField(max_length=100, default="İsimsiz")
    number = models.CharField(max_length=10, default="Numarasız")
    classname = models.ForeignKey(ClassModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.classname.school.name.upper() + ": " + self.classname.name + " - " + self.name + " ({})".format(
            self.number)


class ParentModel(models.Model):
    name = models.CharField(max_length=100, default="İsimsiz")
    telno = models.CharField(max_length=100, default="Numara eklenmemiş.")
    child = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " [{}] ".format(self.child)


class BranchModel(models.Model):
    name = models.CharField(max_length=100, default="Branş Yok")

    def __str__(self):
        return self.name


class TeacherModel(models.Model):
    name = models.CharField(max_length=100, default="İsimsiz")
    branch = models.ManyToManyField(BranchModel)

    def __str__(self):
        return self.name


class CourseModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default="İsimsiz")
    teachers = models.ManyToManyField(TeacherModel, null=True, blank=True)
    students = models.ManyToManyField(StudentModel, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.name
