from django.db import models

class UserDocumentServer(models.Model):
    project_name = models.CharField(max_length=200)
    port_number = models.IntegerField()

    def __str__(self):
        return self.project_name



