"""Container for the various views supported."""

from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from issue_tracker.app import forms
from issue_tracker.app import models as it_models


class CreateIssue(CreateView):
    model = it_models.Issue
    fields = ['title', 'description', 'issue_type', 'priority', 'project',
              'assignee']
    template_name = 'create_issue.html'

    def form_valid(self, form):
        new_issue = form.save(commit=False)
        new_issue.reporter = self.request.user
        # new_issue.date_modified = el
        new_issue.save()
        return HttpResponseRedirect(new_issue.get_absolute_url())


class EditIssue(DetailView):
    model = it_models.Issue
    template_name = 'edit_issue.html'


class ViewIssue(DetailView):
    model = it_models.Issue
    template_name = 'issue_detail.html'


# TODO(jdarrieu): Not done with this work yet.
class SearchIssues(FormView):
    form_class = forms.SearchForm
    template_name = 'search.html'


class MultipleIssues(ListView):
    model = it_models.Issue
    template_name = 'multi_issue.html'
