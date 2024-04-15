from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    HARD_COVER = 'HC'
    SOFT_COVER = 'SC'
    SPECIAL_COVER = 'SPC'
    COVER_CHOICES = [
        (HARD_COVER, _('Hard cover')),
        (SOFT_COVER, _('Soft cover')),
        (SPECIAL_COVER, _('Special cover'))
    ]
    cover = models.CharField(max_length=3, choices=COVER_CHOICES, default=SOFT_COVER, verbose_name=_('cover type'))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    page_count = models.PositiveIntegerField(verbose_name=_("Page Count"))
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', verbose_name=_('author'), null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    image = models.ImageField(upload_to='media/', verbose_name=_("Image"))
    categories = models.ManyToManyField('Category', related_name='books', verbose_name=_('categories'))
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Category Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')