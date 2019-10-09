from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)
    
    class meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
                def __str__(self):
                    return self.email


