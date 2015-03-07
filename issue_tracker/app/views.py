"""Container for the various views supported."""
import datetime

from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from issue_tracker.app import forms
from issue_tracker.app import models as it_models
from issue_tracker.app import filters


class CreateIssue(CreateView):
    model = it_models.Issue
    fields = ['title', 'description', 'issue_type', 'priority', 'project',
              'assignee']
    template_name = 'create_issue.html'

    def form_valid(self, form):
        new_issue = form.save(commit=False)
        new_issue.reporter = self.request.user
        new_issue.date_modified = datetime.datetime.now()
        new_issue.save()
        return HttpResponseRedirect(new_issue.get_absolute_url())


class EditIssue(DetailView):
    model = it_models.Issue
    template_name = 'edit_issue.html'


class ViewIssue(DetailView):
    model = it_models.Issue
    template_name = 'issue_detail.html'


class SearchIssues(FormView):
    form_class = forms.SearchForm
    template_name = 'search.html'
    success_url = '/issue/search/'

    def form_valid(self, form):
        data = filters.filter_issue_results(form.cleaned_data)
        if not data:
            data = []
        return self.render_to_response({'object_list': data,
                                        'page': 'Issue Search'})


class MultipleIssues(ListView):
    model = it_models.Issue
    template_name = 'multi_issue.html'
