from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    preview_image = models.ImageField(upload_to='news_previews/', blank=True, null=True, verbose_name='Превью-картинка')
    short_text = models.TextField(max_length=300, verbose_name='Краткий текст')
    full_text = models.TextField(verbose_name='Полный текст')
    date_published = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    def __str__(self):
        return self.title or f'Фото {self.id}'
    class Meta:
        ordering = ['order']
        verbose_name = 'Фото галереи'
        verbose_name_plural = 'Фото галереи'

class Schedule(models.Model):
    DAYS = [('mon','Понедельник'),('tue','Вторник'),('wed','Среда'),('thu','Четверг'),('fri','Пятница'),('sat','Суббота'),('sun','Воскресенье')]
    PLACE_CHOICES = [('museum','Музей космонавтики'),('korolev','Дом-музей Королёва')]
    place = models.CharField(max_length=20, choices=PLACE_CHOICES, verbose_name='Место')
    day = models.CharField(max_length=3, choices=DAYS, verbose_name='День недели')
    open_time = models.TimeField(blank=True, null=True, verbose_name='Время открытия')
    close_time = models.TimeField(blank=True, null=True, verbose_name='Время закрытия')
    is_closed = models.BooleanField(default=False, verbose_name='Выходной')
    note = models.CharField(max_length=200, blank=True, verbose_name='Примечание')
    def __str__(self):
        return f'{self.get_place_display()} - {self.get_day_display()}'
    class Meta:
        ordering = ['place', 'day']
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

class ExcursionRequest(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    desired_date = models.DateField(verbose_name='Желаемая дата')
    desired_time = models.CharField(max_length=5, choices=[('10:00','10:00'),('12:00','12:00'),('14:00','14:00'),('16:00','16:00')], verbose_name='Время')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    processed = models.BooleanField(default=False, verbose_name='Обработано')
    confirmation_token = models.CharField(max_length=64, blank=True, null=True, unique=True, verbose_name='Токен подтверждения')
    is_confirmed = models.BooleanField(default=False, verbose_name='Подтверждено')
    def __str__(self):
        return f'{self.full_name} - {self.desired_date} {self.desired_time}'
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка на экскурсию'
        verbose_name_plural = 'Заявки на экскурсии'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    def __str__(self):
        return f'Сообщение от {self.name}'
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение из контактов'
        verbose_name_plural = 'Сообщения из контактов'

class SiteSetting(models.Model):
    key = models.CharField(max_length=50, unique=True, verbose_name='Ключ')
    value = models.TextField(verbose_name='Значение')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')
    def __str__(self):
        return self.key
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'