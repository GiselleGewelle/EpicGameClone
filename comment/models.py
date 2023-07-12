from django.db import models

from posts.models import Post


class Comment(models.Model):
<<<<<<< HEAD
    owner = models.ForeignKey('account.CustomUser', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
=======
    owner = models.ForeignKey('account.CustomUser', related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return f'{self.owner} -> {self.post}'
=======
        return f'{self.owner} -> {self.post}'
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
