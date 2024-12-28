from django.db import models

class Element(models.Model):
    date = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)

    bucket = models.CharField(max_length=255, blank=True, null=True)
    galon = models.CharField(max_length=255, blank=True, null=True)
    kilo = models.CharField(max_length=255, blank=True, null=True)
    half_kilo = models.CharField(max_length=255, blank=True, null=True)
    kes = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name or "Unnamed Element"