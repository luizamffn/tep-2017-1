from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateField()
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

    def alterarStatus(self, status):
        self.closed = status
        self.save()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255, null=False)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text

    def votar(self):
        self.votes = self.votes + 1
        self.save()

    def remover(self):
        self.delete()