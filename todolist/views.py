from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponse, Http404

from .models import Task, Done
from .forms import TaskForm


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'latest_tasks_list'
    paginate_by = 10

    def get_queryset(self):
        """Return the last published tasks."""
        queryset = Task.objects
        if 'is_not_done' in self.request.GET:
            if int(self.request.GET['is_not_done']) == 1:
                queryset = queryset.filter(status=0)

        queryset = queryset.order_by('-id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if 'latest_tasks_list' in context:
            new_context = []
            for task in context['latest_tasks_list']:
                try:
                    done = Done.objects.get(task=task)
                except Done.DoesNotExist:
                    done = False
                task.done = done
                new_context.append(task)

            context['latest_tasks_list'] = new_context

        context['is_not_done'] = 0
        if 'is_not_done' in self.request.GET:
            context['is_not_done'] = self.request.GET['is_not_done']
        return context


class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            done = Done.objects.get(task=context['task'])
        except Done.DoesNotExist:
            done = False
        context['task'].done = done

        return context


class TaskCreate(CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'tasks/create.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'tasks/edit.html'
    success_url = '/tasks/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update tasks """
        obj = self.get_object()
        if not obj.owner == self.request.user:
            return redirect('/tasks/')
        return super(TaskUpdate, self).dispatch(request, *args, **kwargs)


class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = 'tasks/delete_confirm.html'

    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        """ Making sure that only authors can update tasks """
        obj = self.get_object()
        if not obj.owner == self.request.user:
            return redirect('/tasks/')
        return super(TaskDelete, self).delete(request, *args, **kwargs)


def mark_done(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    if task.status == 1:
        return redirect('/tasks/{}'.format(task_id))

    task.status = 1
    task.save()

    done = Done(task=task, how_is_done=request.user)
    done.save()
    return redirect('/tasks/{}'.format(task_id))


def mark_undone(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    if task.status == 0:
        return redirect('/tasks/{}'.format(task_id))

    try:
        done = Done.objects.get(task=task)
    except Done.DoesNotExist:
        raise Http404("Done does not exist")

    if request.user == task.owner or request.user == done.how_is_done:
        task.status = 0
        task.save()
        done.delete()

    return redirect('/tasks/{}'.format(task_id))
