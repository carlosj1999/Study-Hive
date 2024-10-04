from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.university.name}"

class Topic(models.Model):
    name = models.CharField(max_length=255)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Flashcard: {self.question[:50]}..."  # Truncate for display
