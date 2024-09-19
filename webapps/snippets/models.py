from django.db import models

class Snippet(models.Model):
    text = models.TextField()  # the text snippet
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp of creation

    def __str__(self):
        return self.text[:50]  # return first 50 characters

