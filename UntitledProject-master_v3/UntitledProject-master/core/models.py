from django.db import models
from django.contrib.auth.models import User


class MetaConfig(models.Model):
  title = models.CharField(max_length=128)
  active_class = models.CharField(max_length=128)


class Person(models.Model):
  name = models.CharField(max_length=128)
  salary = models.IntegerField()
  function = models.CharField(max_length=128)
  owner = models.ForeignKey(User, related_name='people', on_delete=models.CASCADE)


class Project(models.Model):
  name = models.CharField(max_length=128)
  manager = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()


class ProjectData(models.Model):
  project = models.ForeignKey(Project, related_name='data', on_delete=models.CASCADE)
  all_tasks = completed_tasks = value = percentage = 0

  def init(self):
    for task in self.project.tasks.all():
      self.all_tasks += 1
      if task.done:
        self.completed_tasks +=1

    project_days = (self.project.end_date - self.project.start_date).days
    people = list()
    for task in self.project.tasks.all():
      days = project_days
      if not task.responsable.id in people:
        while (days > 0):
          self.value += task.responsable.salary
          days -= 30
        people.append(task.responsable.id)
    for resource in self.project.resources.all():
      self.value += resource.value

    if self.all_tasks == 0:
      self.percentage = 100
    else:
      self.percentage = (float(self.completed_tasks)/float(self.all_tasks))*100


class Task(models.Model):
  name = models.CharField(max_length=128)
  responsable = models.ForeignKey(Person, related_name='tasks', on_delete=models.CASCADE)
  project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
  done = models.BooleanField(default=False)

  def check_done(self):
    self.done = True
    self.save()

  def uncheck_done(self):
    self.done = False
    self.save()


class Resource(models.Model):
  name = models.CharField(max_length=255)
  value = models.IntegerField()
  project = models.ForeignKey(Project, related_name='resources', on_delete=models.CASCADE)