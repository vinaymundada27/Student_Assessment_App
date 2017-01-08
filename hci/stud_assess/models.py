from django.db import models


# Create your models here.
# @python_2_unicode_compatible
# class Question(models.Model):
#     question_text = models.CharField(max_length=300)
#     pub_date = models.DateTimeField('date_published')
#
#     def __str__(self):
#         return self.question_text
#
#
# # @python_2_unicode_compatible
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=300)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text


class Student(models.Model):
    Name = models.CharField(max_length=50)
    Roll_no = models.IntegerField()
    Maths = models.IntegerField()
    IAS = models.IntegerField()
    HCI = models.IntegerField()
    SE = models.IntegerField()
    SC = models.IntegerField()
    IR = models.IntegerField()



