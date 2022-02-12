from django.db import models

# Create your models here.


class BookData(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    published_on = models.DateField(auto_now_add=True)


class BookChapterData(models.Model):

    class DifficultChoices(models.TextChoices):
        EASY = 'easy'
        MEDIUM = 'medium'
        HARD = 'hard'

    book = models.ForeignKey(BookData, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=80)
    is_mcq_available = models.BooleanField(default=False)
    num_of_topics = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DifficultChoices.choices, default=DifficultChoices.EASY)
