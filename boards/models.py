from django.db import models
from django.conf import settings

class BoardPost(models.Model):
    BOARD_CHOICES = [
        ('free', '자유게시판'),
        ('qna',  'Q&A'),
    ]
    board_type  = models.CharField(max_length=10, choices=BOARD_CHOICES, db_index=True)
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_board_type_display()}] {self.title}"

    @property
    def comment_count(self):
        # related_name='comments' 인 BoardComment 를 셉니다
        return self.comments.count()

class BoardComment(models.Model):
    post       = models.ForeignKey(
        BoardPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author     = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} @ {self.post.title}"