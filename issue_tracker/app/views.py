"""Container for the various views supported."""
from django.views.generic import TemplateView


class ExampleView(TemplateView):
    template_name = 'example.html'

    def get(self, request, *args, **kwargs):
        context = {
            'example_value': 'Hello World!',
        }
        return self.render_to_response(context)
