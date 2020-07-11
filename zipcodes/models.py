from django.db import models

class ZipCodes(models.Model):
    zipcode = models.CharField(max_length=20, null=True, blank=True, verbose_name='zipcode', help_text='Example: 6390')

    def __init(self, zipcode):
        self.zipcode = zipcode
    
    def __str__(self):
        return self.zipcode

