from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')
    author = models.CharField('Author', max_length=20, null=True, blank=True)
    is_done = models.BooleanField('Is_done', default=False)

    def __str__(self):
        return self.title

    def change_state(self):
        self.is_done = not self.is_done
        self.save()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'My tasks'
