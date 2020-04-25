from django.db import models

SHIRT = 1
PANTS = 2
SHOE = 3
kind_choices = (
        (SHIRT, 'لباس'),
        (PANTS, 'شلوار'),
        (SHOE, 'کفش'),
    )


def generate_avatar_filename(self, filename):
    url = 'clothingPics/%s/%s' % (self.name, filename)
    return url


class Clothing(models.Model):
    class Meta:
        verbose_name = 'لباس'
        verbose_name_plural = 'لباس'

    size = models.IntegerField()
    color = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    kind = models.IntegerField(choices=kind_choices)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to=generate_avatar_filename, default='default_clothing.jpg')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color + self.kind
