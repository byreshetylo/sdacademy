from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.contrib import messages
from django.views.generic.edit import CreateView
from models import Feedback


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        self.object = form.save()
        message_text = "You have new message from: %s\nSent at: %s\nMessage text:%s" % (
            self.object.from_email,
            self.object.create_date,
            self.object.message
        )
        mail_admins(self.object.subject, message_text)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        return super(FeedbackView, self).form_valid(form)
