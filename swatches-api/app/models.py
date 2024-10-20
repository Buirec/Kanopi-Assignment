from django.db import models
from django.utils import timezone
from datetime import datetime
import uuid

from django.forms import ValidationError

class BaseModel(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

class ColourType(BaseModel):
  VALUE_CHOICES = [
    ('red', 'red'),
    ('green', 'green'),
    ('blue', 'blue'),
    ('hue', 'hue'),
    ('saturation', 'saturation'),
    ('lightness', 'lightness'),
  ]
  
  colour_type = models.CharField(max_length=4)
  
  first_value = models.CharField(max_length=20, choices=VALUE_CHOICES, default="red")
  second_value = models.CharField(max_length=20, choices=VALUE_CHOICES, default="green")
  third_value = models.CharField(max_length=20, choices=VALUE_CHOICES, default="blue")
  
  first_value_max = models.PositiveIntegerField(blank=True, null=True)
  second_value_max = models.PositiveIntegerField(blank=True, null=True)
  third_value_max = models.PositiveIntegerField(blank=True, null=True)