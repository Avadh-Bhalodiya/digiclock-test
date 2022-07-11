from django.db import models

from main import models as main_models
from main import constants as main_constants


class WorkConfig(main_models.BaseModel):
    """
    Model will include the various configs for different companies.

    For example for company x we might want login time at 10 AM in the morning
    and logout time at 7 PM in the evening so this model will have such
    kind of entries.
    """

    name = models.CharField(max_length=100)
    login_time = models.TimeField()
    logout_time = models.TimeField()


class WorkLogs(main_models.BaseModel):
    """
    Model will include the login and logout times for the users.

    It has employee FK and also work description of the day.

    Login or Logout can be figured out by the log_type.

    Work config will be stored with the worklogs because, it might be possible that,
    in future employee may change his company or we should have a record
    for what config we set.
    """

    employee = models.ForeignKey("core.UserProfile", on_delete=models.PROTECT)
    work_description = models.CharField(max_length=1000)
    log_type = models.CharField(max_length=20, choices=main_constants.WORK_CHOISES)
    work_config = models.ForeignKey("employee.WorkConfig", on_delete=models.PROTECT)


class EmployeeConfig(main_models.BaseModel):
    """
    Model will include the mapping for workconfig and employee.
    """

    work_config = models.ForeignKey("employee.WorkConfig", on_delete=models.PROTECT)
    employee = models.ForeignKey("core.UserProfile", on_delete=models.PROTECT)
