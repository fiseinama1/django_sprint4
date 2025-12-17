from django.utils.timezone import now
from django.core.paginator import Paginator
from blog.constants import POSTS_BY_PAGE
from blog.models import Post


def query_post(manager=None, for_author=False):
    """
    for_author=True  - для автора (все посты)
    for_author=False - для других пользователей (только опубликованные)
    """
    if manager is None:
        queryset = Post.objects.all()
    else:
        queryset = manager.all()

    if for_author:
        return queryset.order_by('-pub_date')
    else:
        return queryset.filter(
            is_published=True,
            pub_date__lt=now(),
            category__is_published=True
        ).select_related('author', 'location', 'category'
                         ).order_by('-pub_date')


def posts_pagination(request, queryset):
    """Пагинация на 10 постов на страницу"""
    paginator = Paginator(queryset, POSTS_BY_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
