"""Container for the various views supported."""
import datetime

from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import UpdateView
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

    # new_issue.date_modified should be new_issue.date_submitted.

    def form_valid(self, form):
        new_issue = form.save(commit=False)
        new_issue.reporter = self.request.user
        new_issue.date_modified = datetime.datetime.now()
        new_issue.save()
        return HttpResponseRedirect(new_issue.get_absolute_url())


class EditIssue(UpdateView):
    model = it_models.Issue
    fields = ['title', 'description', 'issue_type', 'priority', 'project',
              'assignee', 'status', 'verifier']
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
            # error = "No Data"  # error text message
        return self.render_to_response({'object_list': data,
                                        'page': 'Issue Search',
                                        # resend form to search page
                                        'form': form,
                                        })

    # TODO(Ted): I add this but it does not work
    def form_invalid(self, form):
        data = filters.filter_issue_results(form.cleaned_data)
        if not data:
            data = []
            error = "No Data"
            # return super(SearchIssues, self).form_valid(form)

        return self.render_to_response({'object_list': data,
                                        'page': 'Issue Search',
                                        'form': form,
                                        'NoDataError': error,
                                        })
        # return super(SearchIssues, self).form_invalid(form)
    # testing form_invalid funcation


class MultipleIssues(ListView):
    model = it_models.Issue
    template_name = 'multi_issue.html'
