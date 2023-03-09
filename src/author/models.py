from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных о пользователе сайта.
    """

    resume_ref = models.URLField(max_length=255, verbose_name="Ссылка на резюме")
    github_ref = models.URLField(max_length=255, verbose_name="Ссылка на GitHub")
    email = models.EmailField(max_length=255, verbose_name="Email адресс")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'
