import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    post_id = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return self.post_id
