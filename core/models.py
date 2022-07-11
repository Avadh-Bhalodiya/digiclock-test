from django.db import models

from main import models as main_models


class UserProfile(main_models.BaseModel):
    mobile_number = models.CharField(max_length=10)
