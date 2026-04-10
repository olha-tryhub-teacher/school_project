from django.views.generic import ListView, DetailView
from .models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'Announcements/announcement_list.html'
    context_object_name = 'announcements'
    paginate_by = 10

    def get_queryset(self):
        return Announcement.objects.filter(is_active=True).order_by('-created_at')


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'Announcements/announcement_detail.html'
    context_object_name = 'announcement'

    # Код з твоєї картинки:
    def get(self, request, *args, **kwargs):
        announcement_id = str(kwargs["pk"])
        viewed = request.session.get("viewed_announcements", [])
        if announcement_id not in viewed:
            obj = self.get_object()
            obj.views_count += 1
            obj.save()
            viewed.append(announcement_id)
            request.session["viewed_announcements"] = viewed

        return super().get(request, *args, **kwargs)
