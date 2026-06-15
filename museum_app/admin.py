from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.conf import settings
from .models import News, GalleryImage, Schedule, ExcursionRequest, ContactMessage, SiteSetting

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'date_published', 'is_published']
    list_filter = ['is_published', 'date_published']
    search_fields = ['title']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['place', 'day', 'open_time', 'close_time', 'is_closed']
    list_filter = ['place', 'is_closed']

@admin.register(ExcursionRequest)
class ExcursionRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'desired_date', 'desired_time', 'created_at', 'is_confirmed', 'processed']
    list_filter = ['is_confirmed', 'processed', 'desired_date']
    search_fields = ['full_name', 'email']
    actions = ['mark_processed', 'mark_confirmed']

    def mark_processed(self, request, queryset):
        queryset.update(processed=True)
    mark_processed.short_description = 'Отметить как обработанные'

    def mark_confirmed(self, request, queryset):
        queryset.update(is_confirmed=True)
    mark_confirmed.short_description = 'Отметить как подтверждённые'

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['key', 'description']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read', 'reply_link')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Отметить как прочитанные'

    def reply_link(self, obj):
        from django.utils.html import format_html
        return format_html('<a class="button" href="{}">✉️ Ответить</a>', f'/admin/museum_app/contactmessage/{obj.id}/reply/')
    reply_link.short_description = 'Ответить'
    reply_link.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:message_id>/reply/', self.admin_site.admin_view(self.reply_view), name='contactmessage_reply'),
        ]
        return custom_urls + urls

    def reply_view(self, request, message_id):
        message = get_object_or_404(ContactMessage, id=message_id)
        if request.method == 'POST':
            subject = request.POST.get('subject', 'Ответ из музея космонавтики')
            reply_text = request.POST.get('reply_text')
            if reply_text:
                html_message = render_to_string('email/reply_email.html', {
                    'name': message.name,
                    'reply_text': reply_text,
                })
                plain_message = strip_tags(html_message)
                send_mail(
                    subject=subject,
                    message=plain_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[message.email],
                    html_message=html_message,
                    fail_silently=False,
                )
                message.is_read = True
                message.save()
                messages.success(request, f'Ответ отправлен на {message.email}')
                return redirect('admin:museum_app_contactmessage_changelist')
            else:
                messages.error(request, 'Введите текст ответа')
        return render(request, 'admin/reply_to_message.html', {'message': message})