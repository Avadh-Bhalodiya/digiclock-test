import logging

from django.db import models

logger = logging.getLogger(__name__)


class Manager(models.Manager):
    def dfilter(self, *args, **kwargs):
        return self.filter(is_deleted=False, **kwargs)


class BaseModel(models.Model):
    """
    This model adds the default created, update and is_deleted fields into all the models.

    Always extend this model instance into Django models.

    is_deleted field is added because, to delete any row may currupt the dataase.
    There might be some records attached to FK and that might raise the error.
    Now to overcome that we can use cascade delete but it can remove the
    related rows as well. So here, we have overriden the delete method.
    So on all the delete call, we will simply mark deleted as true.

    Moreover, there is a dfilter which we will always use in the database.

    While doing the coding, always use models.ModelName.objects.dfilter() instead of
    filter.
    """

    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = Manager()

    def delete(self):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    class Meta:
        abstract = True
