
from django import forms
from django.contrib.auth.models import User

from issue_tracker.app.models import STATUSES
from issue_tracker.app.models import TYPES
from issue_tracker.app.models import PRIORITIES

class SearchForm(forms.Form):
    """Search for issues based on provided criteria."""
    keywords = forms.CharField(
        help_text='Keyword search of issue title and description',
        required=False)
    status = forms.ChoiceField(choices=STATUSES, required=False)
    issue_type = forms.ChoiceField(choices=TYPES, required=False)
    priority = forms.ChoiceField(choices=PRIORITIES, required=False)

    
    submitted_date = forms.DateTimeField(
        help_text='Date issue was created', required=False)
    modified_date = forms.DateTimeField(
        help_text='Date issue was last modified', required=False)
    closed_date = forms.DateTimeField(help_text='Date issue was closed',
                                      required=False)

    reporter = forms.ModelChoiceField(queryset=User.objects.all(),
                                      required=False)
    assignee = forms.ModelChoiceField(queryset=User.objects.all(),
                                      required=False)
