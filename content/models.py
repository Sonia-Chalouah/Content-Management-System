from django.db import models

class WordPhrase(models.Model):
    word_phrase = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    example_sentence = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.word_phrase
