import datetime
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
  config = MetaConfig(title="Home page", active_class="index")
  projects = Project.objects.filter(manager=request.user).order_by('-id')
  data = list()
  for project in projects:
    project_data = ProjectData(project=Project.objects.get(id=project.id))
    project_data.init()
    data.append(project_data)
  return render(request, 'index.html', {'projects': projects, 'data': data, 'user': get_current_user(request), 'config': config})


@login_required
def projects(request):
  config = MetaConfig(title="Projects", active_class="projects")
  projects = Project.objects.filter(manager=request.user).order_by('-id')
  return render(request, 'projects.html', {'projects': projects, 'user': get_current_user(request), 'config': config})


@login_required
def project_detail(request, project_id):
  config = MetaConfig(title="Project detail", active_class="projects")
  project = Project.objects.get(id=project_id)
  tasks = Task.objects.filter(project=project)
  project_data = ProjectData(project=project)
  project_data.init()

  return render(request, 'project_detail.html', {'project': project,
                                                 'project_data': project_data,
                                                 'tasks': tasks,
                                                 'user': get_current_user(request),
                                                 'config': config})


@login_required
def person_detail(request, person_id):
  config = MetaConfig(title="Person detail", active_class="people")
  person = Person.objects.get(id=person_id)
  tasks = Task.objects.filter(responsable=person)

  return render(request, 'person_detail.html', {'person': person,
                                                'tasks': tasks,
                                                'user': get_current_user(request),
                                                'config': config})


@login_required
def resource_detail(request, resource_id):
  config = MetaConfig(title="Resource detail", active_class="resources")
  resource = Resource.objects.get(id=resource_id)

  return render(request, 'resource_detail.html', {'resource': resource,
                                                  'user': get_current_user(request),
                                                  'config': config})


@login_required
def people(request):
  config = MetaConfig(title="People", active_class="people")
  people = Person.objects.filter(owner=request.user).order_by('-id')
  return render(request, 'people.html', {'people': people, 'user': get_current_user(request), 'config': config})


@login_required
def tasks(request):
  config = MetaConfig(title="Tasks", active_class="tasks")
  people = Person.objects.filter(owner=request.user)
  projects = Project.objects.filter(manager=request.user)
  tasks = Task.objects.filter(project__in=projects).order_by('-id')
  return render(request, 'tasks.html', {'tasks': tasks,
                                             'projects': projects,
                                             'people': people,
                                             'user': get_current_user(request),
                                             'config': config})


@login_required
def resources(request):
  config = MetaConfig(title="Resources", active_class="resources")
  projects = Project.objects.filter(manager=request.user)
  resources = Resource.objects.filter(project__in=projects).order_by('-id')
  return render(request, 'resources.html', {'resources': resources,
                                            'projects': projects,
                                            'user': get_current_user(request),
                                            'config': config})


@login_required
def check_task(request, task_id):
  task = Task.objects.get(id=task_id)
  task.check_done()
  return redirect('tasks')


@login_required
def uncheck_task(request, task_id):
  task = Task.objects.get(id=task_id)
  task.uncheck_done()
  return redirect('tasks')


@login_required
def delete_task(request, task_id):
  task = Task.objects.get(id=task_id)
  task.delete()
  return redirect('tasks')


@login_required
def delete_project(request, project_id):
  project = Project.objects.get(id=project_id)
  project.delete()
  return redirect('projects')


@login_required
def delete_resource(request, resource_id):
  resource = Resource.objects.get(id=resource_id)
  resource.delete()
  return redirect('resources')


@login_required
def delete_person(request, person_id):
  person = Person.objects.get(id=person_id)
  person.delete()
  return redirect('people')


@login_required
def get_current_user(request):
  return request.user


class RegisterUserView(View):
  template = 'login.html'

  def get(self, request):
    return render(request, self.template)

  def post(self, request):
    form = RegisterUserForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      user = User.objects.create_user(username=data['username'], email=data['email'],
                                      password=data['password'], first_name=data['name'])
      return redirect('index')

    return render(request, self.template, {'form': form})


class NewProjectView(View):
  template = 'projects.html'

  def get(self, request):
    return render(request, self.template)

  def post(self, request):
    form = NewProjectForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      start_date = datetime.datetime.strptime(data['start_date'], '%d %B, %Y')
      end_date = datetime.datetime.strptime(data['end_date'], '%d %B, %Y')
      project = Project(name=data['name'], description=data['description'], start_date=start_date, end_date=end_date,
                        manager=request.user)
      project.save()
      return redirect('projects')

    return render(request, self.template, {'form': form})


class NewPersonView(View):
  template = 'people.html'

  def get(self, request):
    return render(request, self.template)

  def post(self, request):
    form = NewPersonForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      person = Person(name=data['name'], salary=data['salary'], function=data['function'], owner=request.user)
      person.save()
      return redirect('people')

    return render(request, self.template, {'form': form})


class NewTaskView(View):
  template = 'tasks.html'

  def get(self, request):
    return render(request, self.template)

  def post(self, request):
    form = NewTaskForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      person = Person.objects.get(id=data['responsable_id'])
      project = Project.objects.get(id=data['project_id'])
      task = Task(name=data['name'],
                          responsable=person,
                          project=project)
      task.save()
      return redirect('tasks')

    return render(request, self.template, {'form': form})


class NewResourceView(View):
  template = 'resources.html'

  def get(self, request):
    return render(request, self.template)

  def post(self, request):
    form = NewResourceForm(request.POST)

    if form.is_valid():
      data = form.cleaned_data
      project = Project.objects.get(id=data['project_id'])
      resource = Resource(name=data['name'],
                          value=data['value'],
                          project=project)
      resource.save()
      return redirect('resources')

    return render(request, self.template, {'form': form})