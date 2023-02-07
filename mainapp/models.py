from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Todo (models.Model):
    name = models.CharField(max_length=120,verbose_name='категории')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(verbose_name='Дата окончание')
    image = models.ImageField(
        upload_to='todo/image/', verbose_name='Картинки'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='todoes',verbose_name='Пользователь'
    )
    is_done = models.BooleanField(default=False, 
                                  verbose_name='Готово ли?'
    )

    def __str__(self):
        return self.name


    

    
