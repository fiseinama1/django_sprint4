from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Post, Comment

User = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text', 
            'pub_date',       
            'is_published',   
            'category',
            'location',
            'image'
        ]
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local', 
                    'class': 'form-control',
                    'id': 'id_pub_date'
                }
            ),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'id_is_published'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Простые настройки
        self.fields['is_published'].label = 'Опубликовано'
        self.fields['pub_date'].label = 'Дата публикации'
        
        # Добавляем CSS классы всем полям автоматически
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs.update({'class': 'form-control'})
        
        # Автозаполнение времени с коррекцией
        if not self.instance.pk:
            from datetime import timedelta
            now = timezone.now() + timedelta(hours=4)  # +4 часа
            self.initial['pub_date'] = now.strftime('%Y-%m-%dT%H:%M')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
