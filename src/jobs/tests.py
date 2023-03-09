from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работы
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.
        :return:
        """

        Job.objects.create(
            image="job_img",
            description="some job",
            detail_description="Some text about new job",
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей работы.
        :return:
        """

        job = Job.objects.get(description="some job")

        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
