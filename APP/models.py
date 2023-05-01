from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

# user = User.objects.create_user("priyanshu","pushpendra@gmail.com","121212")

class College(models.Model):
    college_id = models.CharField(max_length=12 , default=7388006830)
    college_name = models.CharField(max_length=100 , default="Dnyan Ganga Degree College")
    college_address = models.TextField()
    college_contact = models.IntegerField(10)

    def __str__(self):
        return self.college_name + " ," +  self.college_address 


class Student(models.Model):
    std_id = models.CharField(max_length=10)
    std_name = models.CharField(max_length=100)
    std_address = models.TextField()
    std_contact = models.IntegerField(10)
    college = models.ForeignKey(College , on_delete=models.CASCADE)

    def __str__(self):
        return self.std_name

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=100)
    teacher_address = models.TextField()
    teacher_contact = models.IntegerField(10)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name



class ClassRoom(models.Model):
    college_name = models.ForeignKey(College,on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    class_std = models.CharField(max_length=100 , default="BSC-IT")
    created_at = models.DateField(auto_now_add=True)
    action = models.BooleanField(default=False)

    def __str__(self):
        return self.class_std



    