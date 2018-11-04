from django.db import models
from django.utils import timezone

from datetime import datetime
from random import choices

#model for academic staffs
class A_staff(models.Model):
    assistant_lec = 'as'
    lecturer_one = 'lo'
    lecturer_two = 'lt'
    senior_lec = 'sl'
    reader = 'rd'
    professor = 'pf'

    rank_choice = (
        ("assistant_lec" , "Assistant lecturer"),
        ("lecturer_one" , "Lecturer one"),
        ("lecturer_two" , "Lecturer two"),
        ("senior_lec" , "Senior lecturer"),
        ("reader" , "Reader"),
        ("professor" , "Professor"),
      )

    faculty_choice = (
        ("science" , "Medical science"),
        ("engineering" , "engineering"),
      )
    
    score_choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )

    name = models.CharField("staff name",max_length=64)
    dFirstAppointment = models.DateField("Date of first appointment")
    rank = models.CharField("Rank", max_length = 30, choices=rank_choice , default="assistant_lec")
    qualification = models.CharField("Top Qualification",max_length=30)
    salaryGLevel = models.IntegerField("Salary grade Level",blank=False)
    step = models.IntegerField("Step", blank=False)
    yLastPromotion = models.DateField("Year of last promotion")
    pressentYear = models.DateField("Present Year")
    teachingE = models.IntegerField("Teaching Effectiveness",blank=False, choices=score_choices, default=1)
    publicationS = models.IntegerField("Publication Score",blank=False, choices=score_choices, default=1)
    responsibilityS = models.IntegerField("Responsibility Score",blank=False, choices=score_choices, default=1)
    totalScore = models.IntegerField("Total score",blank=False)
    nYearsPresentG = models.IntegerField("No of years on present grade",blank=True)
    duePromotion = models.BooleanField("Due Promotion")
    systemRecomUpgrade = models.CharField("System Upgrade", max_length=20)

    avater = models.FileField("Profile image", upload_to='picture', blank = True)
    pub = models.TextField("Publications in Previous Years e.g(books)", default='No publication yet')
    faculty = models.CharField("Rank", max_length = 30, choices=faculty_choice , default="science")
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Academic Staff Database"


    def __str__(self):
            return f"({ self.name} ({self.rank}))"


# model for none academic staffs
class None_A_staff(models.Model):

    
    score_choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )

    name = models.CharField("staff name",max_length=100)
    dFirstAppointment = models.DateField("Date of first appointment")
    qualification = models.CharField("Top Qualification",max_length=30)
    salaryGLevel = models.IntegerField("Salary grade Level",blank=False)
    step = models.IntegerField("Step", blank=False)
    yLastPromotion = models.DateField("Year of last promotion")
    pressentYear = models.DateField("Present Year")
    responsibilityS = models.IntegerField("Responsibility Score",blank=False, choices=score_choices, default=1)
    totalScore = models.IntegerField("Total score",blank=False)
    nYearsPresentG = models.IntegerField("No of years on present grade",blank=True)
    duePromotion = models.BooleanField("Due Promotion")
    systemRecomUpgrade = models.CharField("System Upgrade",max_length = 20)
    a_pcRecom = models.CharField("A and PC recommendation", max_length=20)
    
    avater = models.FileField("Profile image", upload_to='picture', blank = True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "None Academic Staff Database"


    def __str__(self):
            return f"{ self.name} {' '} ({'None academic'}))"

    
