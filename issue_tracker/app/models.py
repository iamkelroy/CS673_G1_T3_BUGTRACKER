from django.contrib.auth import models as auth_models
from django.core.urlresolvers import reverse
from django.db import models

STATUSES = (('new', 'New',),
            ('assigned', 'Assigned',),
            ('accepted', 'Accepted',),
            ('fixed', 'Fixed',),
            ('verified', 'Verified',),
            ('wai', 'Working as Intended',),
            ('obsolete', 'Obsolete',),
            ('duplicate', 'Duplicate',),
            )

TYPES = (('bug', 'Bug',),
         ('feature', 'Feature Request',),
         ('internal_cleanup', 'Internal Cleanup',),
         )

PRIORITIES = (('p1', 'P1',),
              ('p2', 'P2',),
              ('p3', 'P3',),
              ('p4', 'P4',),
              )


# TODO(jdarrieu): Dummied up, waiting for other team to provide.
PROJECTS = (('1', 'Dummy project1',),
            ('2', 'Dummy project2',),
            )


class Issue(models.Model):
    """Issue"""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    issue_type = models.CharField(max_length=20, choices=TYPES)
    status = models.CharField(max_length=20, default='New', choices=STATUSES)
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    project = models.CharField(max_length=100, blank=True, choices=PROJECTS)
    # Dates
    submitted_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(null=True, editable=False)
    # Users
    reporter = models.ForeignKey(auth_models.User, related_name='reporter',
                                 null=True)
    assignee = models.ForeignKey(auth_models.User, related_name='assignee',
                                 blank=True, null=True)
    verifier = models.ForeignKey(auth_models.User, related_name='verifier',
                                 blank=True, null=True)

    class Meta(object):
        ordering = ['id']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_issue', kwargs={'pk': self.pk})
