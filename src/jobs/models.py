"""
Модели для приложения "Jobs" (выполненные работы).
"""

from django.db import models

from base.models import TimeStampMixin
from ckeditor_uploader.fields import RichTextUploadingField


class Job(TimeStampMixin):
    """
    Модель для хранения данных о работах.
    """

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Изображение для демонстрации работы",
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание",
        help_text="Краткое описание выполненной работы",
    )
    detail_description = RichTextUploadingField(
        max_length=512,
        default="Выполненная работа",
        verbose_name="Детальное описание",
        help_text="Детальное описание выполненной работы",
    )

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"

    def __str__(self) -> str:
        return f'Объект "Выполненная работа" (id={self.pk})'
