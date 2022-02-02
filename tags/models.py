from django.db import models

# Create your models here.

#Tag

class Tag(models.Model):
    label = models.CharField(max_length=255)


# Tagged Items

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)