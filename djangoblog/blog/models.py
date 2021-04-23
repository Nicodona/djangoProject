from django.urls import reverse
from django.db import models

class POst(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
