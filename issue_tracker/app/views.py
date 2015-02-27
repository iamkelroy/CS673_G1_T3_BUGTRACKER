"""Container for the various views supported."""

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from issue_tracker.app import forms
from issue_tracker.app import models as it_models


class ExampleView(TemplateView):
    template_name = 'issue_page.html'

    def get(self, request, *args, **kwargs):
        context = {
            'example_value': 'Hello World!',
        }
        return self.render_to_response(context)


class CreateIssue(CreateView):
    model = it_models.Issue
    fields = ['title', 'description', 'issue_type', 'priority', 'project',
              'assignee']
    template_name = 'Create_Issue_Bootstrap.html'

    def form_valid(self, form):
        new_issue = form.save(commit=False)
        new_issue.reporter = self.request.user
        # new_issue.date_modified = el
        new_issue.save()
        return HttpResponseRedirect(new_issue.get_absolute_url())


class ViewIssue(DetailView):
    model = it_models.Issue
    template_name = 'issue_page.html'


# TODO(jdarrieu): Not done with this work yet.
class SearchIssues(FormView):
    form_class = forms.SearchForm
    template_name = 'search.html'


# Created to testing Issue Index template (JWA).
# class ListIssues(TemplateView):
#     model = it_models.Issue
#     template_name = 'issue_index.html'


def IndexIssues(request):
    issues_list = it_models.Issue.objects.order_by('pk')
    template = loader.get_template('issue_index.html')
    context = RequestContext(request, {
        'issues_list': issues_list,
    })
    return HttpResponse(template.render(context))

def CreateIssues(request):
    issues_list = it_models.Issue.objects.order_by('pk')
    template = loader.get_template('Create_Issue_Bootstrap.html')
    context = RequestContext(request, {
        'issues_list': issues_list,
    })
    return HttpResponse(template.render(context))


