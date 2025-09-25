from django.db import models

class Slot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} {self.time} - {self.description}"
    
class reg_tbl(models.Model):
    fname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=10, null=True, blank=True)
    cpassword = models.CharField(max_length=10, null=True, blank=True)

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('canceled', 'Canceled'),
        ('rescheduled', 'Rescheduled'),
    ]

    user = models.ForeignKey(reg_tbl, on_delete=models.CASCADE)
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)  # one booking per slot
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.user.fname} on {self.slot.date} at {self.slot.time}"
