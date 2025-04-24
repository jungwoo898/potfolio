from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator
from .models import BoardPost, BoardComment

def post_list(request, board_type):

    qs = (
        BoardPost.objects
        .filter(board_type=board_type)
        .annotate(comment_count=Count('comments'))
    )

    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page')       # ?page=2
    page_obj = paginator.get_page(page_number)  # page_obj 정의!

    board_name = dict(BoardPost.BOARD_CHOICES)[board_type]
    return render(request, 'boards/post_list.html', {
        'page_obj': page_obj,                       # 여기에 page_obj 넘기기
        'paginator': paginator,
        'is_paginated': page_obj.has_other_pages(),
        'board_type': board_type,
        'board_name': board_name,
    })

@login_required
def post_add(request, board_type):
    if request.method == 'POST':
        title   = request.POST['title']
        content = request.POST['content']
        post = BoardPost.objects.create(
            board_type=board_type,
            title=title,
            content=content,
            author=request.user,
        )
        return redirect('boards:post_detail', board_type=board_type, post_id=post.id)
    return render(request, 'boards/post_form.html', {'board_type': board_type})

def post_detail(request, board_type, post_id):
    post = get_object_or_404(BoardPost, board_type=board_type, id=post_id)

    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get("comment")
        if content:
            BoardComment.objects.create(post=post, author=request.user, content=content)
        return redirect('boards:post_detail', board_type=board_type, post_id=post.id)

    comments   = post.comments.all()
    board_name = dict(BoardPost.BOARD_CHOICES)[board_type]
    # 상세에도 comment_count를 넘겨주면 템플릿에서 바로 쓸 수 있습니다
    return render(request, 'boards/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_count': comments.count(),
        'board_name': board_name,
    })