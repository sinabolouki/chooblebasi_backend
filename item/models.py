from django.db import models

# Create your models here.
class Clothe (models.Model):
    class Meta:
        verbose_name = 'لباس'
        verbose_name_plural= 'لباس'
    size = models.IntegerField()
    color = models.CharField(max_length = 20)
    SHIRT = 1
    PANTS = 2
    SHOE = 3
    kind_choices = (
    (SHIRT , 'لباس') ,
    (PANTS , 'شلوار'),
    (SHOE , 'کفش'),
    )
    kind = models.IntegerField(choices=kind_choices)
    def __str__(self):
        return self.color + self.kind
