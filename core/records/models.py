from django.db import models
from userauth.models import User

EMPLOYMENT_STATUS = (
    ("full-time", "Full-Time"),
    ("part-time", "Part-Time")
)

SOURCES = (
   ( "wellfound", "Wellfound"),
   ("linkedin", "LinkedIn"),
   ("otta", "Otta"),
   ("indeed", "Indeed")
)

# Create your models here.
class Application(models.Model):
    # This should be the current date by default (on frontend) but user should be able to change
    date = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=25, choices=EMPLOYMENT_STATUS, default='full time')
    salary_min = models.IntegerField(null=True)
    salary_max = models.IntegerField(null=True)
    location = models.CharField(max_length=100)
    is_confirmed = models.BooleanField(default=False)
    source = models.CharField(max_length=25, choices=SOURCES)
    link = models.CharField(max_length=200, null=True)
    follow_up_date_1 = models.DateField(null=True)
    follow_up_date_2 = models.DateField(null=True)
    has_received_response = models.BooleanField(default=False)
    has_received_interview_invitation = models.BooleanField(default=False)
    was_rejected = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Record of {self.user.first_name} application to {self.company} for {self.position} role"


