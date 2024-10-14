from doctest import FAIL_FAST
from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=255, null=False, blank=False
    )
    created_at = models.DateTimeField(
        verbose_name="Criado em", auto_now_add=True, null=False, blank=False
    )
    deadline = models.DateField(
        verbose_name="Prazo", null=False, blank=False
    )
    finished_at = models.DateField(
        verbose_name="Finalizado em", null=True
    )

    class Meta:
        ordering = ["deadline"]

    def mark_as_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()