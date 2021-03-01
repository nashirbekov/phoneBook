from django.db.models import Q
from django.views.generic import ListView

from .models import Phone


class PhonesView(ListView):
    """Список номеров"""

    model = Phone
    queryset = Phone.objects.all()
    template_name = "phone_list.html"
    paginate_by = 3


class Search(ListView):
    """Поиск номеров"""
    paginate_by = 3
    model = Phone
    template_name = "phone_list.html"

    def get_queryset(self):
        return Phone.objects.filter(
            Q(name__icontains=self.request.GET.get("q")) | Q(phonenumber__icontains=self.request.GET.get("q"))
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
