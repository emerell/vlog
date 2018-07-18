from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
import logging

log = logging.getLogger(__name__)


class BaseView(TemplateView):
    template_name = ''

    log.debug("Hey there debug works!!")
    log.info("Hey there info works!!")
    log.warning("Hey there warning works!!")
    log.error("Hey there error works!!")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)