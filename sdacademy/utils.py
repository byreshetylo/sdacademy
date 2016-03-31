class MyCustomTitleMixin(object):
    custom_title = 'Default custom title'

    def get_context_data(self, **kwargs):
        context = super(MyCustomTitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.custom_title
        return context
