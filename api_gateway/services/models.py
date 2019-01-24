from django.db import models


# Create your models here.

class Services(models.Model):
    """
        Description: A service model for storing all services name and IP address

        Key Features:
            - Store name, IP address

        Attributes:
              - service_name: A service name
              - service_url: Service base location
              - created_at:  Service creation date time
    """
    service_name = models.CharField(max_length=100)
    service_url = models.URLField()
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.service_name) + " " + str(self.service_url)
