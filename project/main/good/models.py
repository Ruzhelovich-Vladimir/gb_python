from django.db import models

# Create your models here.


class good(models.Model):

    title = models.CharField(
        verbose_name=u'Наименование товара',
        max_length=255
    )

    delivery_at = models.DateField(
        verbose_name=u'Дата поступления',
        auto_created=True,
        auto_now_add=True
    )

    price = models.DecimalField(
        verbose_name=u'Цена',
        max_digits=10,
        decimal_places=2,
    )

    unit = models.CharField(
        verbose_name=u'Ед. измерения',
        max_length=10
    )

    type = models.CharField(
        verbose_name=u'Вид товара',
        max_length=255
    )

    weight = models.FloatField(
        verbose_name=u'Вес',
        default=0
    )

    volume = models.FloatField(
        verbose_name=u'Объём',
        default=0
    )

    qty_per_pack = models.PositiveIntegerField(
        verbose_name=u'Количество в упаковке',
        default=0
    )

    manufacturer = models.CharField(
        verbose_name=u'Производитель',
        max_length=255
    )

    distributor = models.CharField(
        verbose_name=u'Поставщик',
        max_length=255
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'
