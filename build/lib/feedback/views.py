from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from wechat_member.views import WxMemberView
from .models import Feedback

class IndexView(WxMemberView, CreateView):
    model = Feedback
    fields = ['type','content']
    success_url = reverse_lazy('feedback:success')
    def form_valid(self, form):
        form.instance.member_id = self.request.session['wx_member']['id']
        return super(IndexView, self).form_valid(form)

class SuccessView(TemplateView):
    template_name = 'feedback/success.html'
