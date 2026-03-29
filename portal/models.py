from django.db import models

# Create your models here.
from django.db import models
import uuid

class Complaint(models.Model):
    complaint_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    mobile = models.CharField(max_length=10)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.complaint_id)