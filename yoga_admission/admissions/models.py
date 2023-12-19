from django.db import models

class YogaParticipant(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    batch_choices = [
        ('6-7AM', '6-7AM'),
        ('7-8AM', '7-8AM'),
        ('8-9AM', '8-9AM'),
        ('5-6PM', '5-6PM'),
    ]
    selected_batch = models.CharField(max_length=10, choices=batch_choices)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.selected_batch}'