from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)

    # def save(self,*args, **kwargs):
    #     if not self.slug:
    #         self.slug = self.name
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.name