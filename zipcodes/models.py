from django.db import models

class ZipCodes(models.Model):
    zipcode = models.CharField(max_length=20, null=True, blank=True, verbose_name='Zipcode', help_text='Example: 6390')

    def __str__(self):
        return 'Landing Content'

