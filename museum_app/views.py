import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse
from .forms import ExcursionForm, FeedbackForm
from .models import News, GalleryImage, Schedule, ExcursionRequest, SiteSetting, ContactMessage

def home(request):
    news_list = News.objects.filter(is_published=True)[:3]
    welcome_text = SiteSetting.objects.filter(key='welcome_text').first()
    gallery_images = GalleryImage.objects.all()[:6]
    return render(request, 'museum_app/home.html', {
        'news_list': news_list,
        'welcome_text': welcome_text.value if welcome_text else '',
        'gallery_images': gallery_images,
    })

def about(request):
    gallery_images = GalleryImage.objects.all()
    about_text = SiteSetting.objects.filter(key='about_text').first()
    return render(request, 'museum_app/about.html', {
        'gallery_images': gallery_images,
        'about_text': about_text.value if about_text else '',
    })

def schedule(request):
    museum_schedule = Schedule.objects.filter(place='museum')
    korolev_schedule = Schedule.objects.filter(place='korolev')
    return render(request, 'museum_app/schedule.html', {
        'museum_schedule': museum_schedule,
        'korolev_schedule': korolev_schedule,
    })

def news_list(request):
    news = News.objects.filter(is_published=True)
    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'museum_app/news_list.html', {'page_obj': page_obj})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    return render(request, 'museum_app/news_detail.html', {'news_item': news_item})

def contacts(request):
    phone = SiteSetting.objects.filter(key='phone').first()
    email = SiteSetting.objects.filter(key='contact_email').first()
    address = SiteSetting.objects.filter(key='address').first()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('museum_app:contacts')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = FeedbackForm()
    return render(request, 'museum_app/contacts.html', {
        'phone': phone.value if phone else '',
        'email': email.value if email else '',
        'address': address.value if address else '',
        'form': form,
    })

def excursion_request(request):
    if request.method == 'POST':
        form = ExcursionForm(request.POST)
        if form.is_valid():
            excursion = form.save(commit=False)
            excursion.confirmation_token = uuid.uuid4().hex
            excursion.is_confirmed = False
            excursion.save()
            confirm_url = request.build_absolute_uri(
                reverse('museum_app:confirm_excursion', args=[excursion.confirmation_token])
            )
            send_mail(
                subject='Подтверждение заявки на экскурсию',
                message=f'Здравствуйте, {excursion.full_name}!\n\nДля подтверждения заявки перейдите по ссылке:\n{confirm_url}\n\nЕсли вы не оставляли заявку, проигнорируйте это письмо.\n\nС уважением, Музей космонавтики.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[excursion.email],
                fail_silently=False,
            )
            messages.success(request, 'Заявка отправлена! Проверьте почту для подтверждения.')
            return redirect('museum_app:excursion_request')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ExcursionForm()
    return render(request, 'museum_app/excursion_request.html', {'form': form})

def confirm_excursion(request, token):
    try:
        excursion = ExcursionRequest.objects.get(confirmation_token=token, is_confirmed=False)
        excursion.is_confirmed = True
        excursion.save()
        messages.success(request, 'Заявка подтверждена! Спасибо.')
    except ExcursionRequest.DoesNotExist:
        messages.error(request, 'Неверная или уже использованная ссылка.')
    return redirect('museum_app:home')

def virtual_tour(request):
    return render(request, 'museum_app/virtual_tour.html')

def quiz(request):
    return render(request, 'museum_app/quiz.html')