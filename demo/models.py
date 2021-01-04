from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0,max_digits=5, decimal_places=2)

    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title


# TODO: Om du vill får du lägga till lite relationer till nya objekt (t.ex. författare, karaktärer eller annat.)
#  Jag har koll på django onetoone, onetomany och manytomany sedan innan så orkade inte göra den delen av tutorialen.
#  Hur man serializeade dem för APIn var lite weird.
