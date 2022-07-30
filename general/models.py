from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated')
    active = models.BooleanField(default=False)


class Slider(BaseModel):
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/Sliders')
    link = models.URLField()
