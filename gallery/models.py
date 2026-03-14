from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=200, help_text="Link to the  project (e.g., GitHub, live demo)")
    order = models.IntegerField(default=0, help_text="Used to sort the gallery")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']