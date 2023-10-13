from django.http import JsonResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import json
from .models import Post, Comment
from django.db.models import Count
from django.shortcuts import get_object_or_404 as get_or_404

POSTS = [
    {
        'title': 'My First Post',
        'text': 'This is my first blog post.',
    },
    {
        'title': 'My Second Post',
        'text': 'This is my second blog post.',
    },
    {
        'title': 'My Third Post',
        'text': 'This is my third blog post.',
    },
    {
        'title': 'My Fourth Post',
        'text': 'This is my fourth blog post.',
    }
]


def parse_post(post: Post):
    return {
        'id': post.id,
        'title': post.title,
        'text': post.text,
    }


def my_posts(request, post_id):
    result_dict = {
        'result': [],
        'filter_by_id': [],
        'result_count': []
    }
    posts = models.Post.objects.all().order_by('-id')
    for post in posts:
        result_dict['result'].append(parse_post(post))

    result_dict['count'] = posts.count()
    result_count = posts.values('id').annotate(count=Count('id')).order_by('id')
    for item in posts.filter(id__gt=post_id):
        result_dict['filter_by_id'].append(parse_post(item))
    return JsonResponse(
        {'posts': result_dict['result'], 'count': result_dict['count'], 'filter_by_id': result_dict['filter_by_id'],
         'result_count': result_dict['result_count']})


def create_post(request):
    title = json.loads(request.body.decode('utf-8')).get('title', '')
    text = json.loads(request.body.decode('utf-8')).get('text', '')

    new_post = Post(title=title, text=text)
    new_post.save()

    return JsonResponse({'id': new_post.id, 'title': new_post.title, 'text': new_post.text}, status=201)


def update_post(request, post_id):
    post = get_or_404(Post, id=post_id)
    post.title = json.loads(request.body.decode('utf-8')).get('title', '')
    post.text = json.loads(request.body.decode('utf-8')).get('text', '')
    post.save()
    return JsonResponse({'id': post.id, 'title': post.title, 'text': post.text})


def delete_post(request, post_id):
    post = get_or_404(Post, id=post_id)
    post.delete()
    return JsonResponse({'post': 'deleted'})


def get_one_post(request, post_id):
    post = get_or_404(Post, id=post_id)
    return JsonResponse({'id': post.id, 'title': post.title, 'text': post.text})


def check_if_exists(request, post_id):
    post = Post.objects.filter(id=post_id).exists()
    return JsonResponse({'exists': post})


def get_or_create(request, post_id):
    post, is_created = Post.objects.get_or_create(
        id=post_id,
        defaults={'title': 'new title', 'text': 'new text'}
    )

    return JsonResponse({'id': post.id, 'title': post.title, 'text': post.text, 'is_created': is_created})


def update_or_create(request, post_id):
    post, is_created = Post.objects.update_or_create(
        id=post_id,
        defaults={'title': 'new title', 'text': 'new text'}
    )

    return JsonResponse({'id': post.id, 'title': post.title, 'text': post.text, 'is_created': is_created})


def filter_and_update(request):
    filtered_posts = Post.objects.filter(title__contains='New')

    updated_posts = []

    for post in filtered_posts:
        post.title = 'new title'
        post.save()
        updated_posts.append({'id': post.id, 'title': post.title, 'text': post.text})

    return JsonResponse({'updated_posts': updated_posts})


def create_comment(request):
    post_id = json.loads(request.body.decode('utf-8')).get('post_id', '')
    text = json.loads(request.body.decode('utf-8')).get('text', '')

    # save
    post = Comment(post_id=post_id, text=text)
    post.save()

    # Comment.objects.bulk_create([post1])
    # Post.objects.bulk_create([post])
    # bulk_update
    return JsonResponse({'id': post.id, 'text': post.text, 'post': post.post_id})


def get_comment_by_post(request, posts_id):
    # post = Post(id=posts_id)
    # comments = Comment.objects.filter(post_id=post)

    post = Post.objects.get(id=posts_id)
    comments = post.comments.all()

    result = []

    for comment in comments:
        result.append({'id': comment.id, 'text': comment.text, 'post_id': comment.post_id})

    return JsonResponse({'comments': result})


def change_status_comment_by_post_id(request, post_id, status):
    comment = Comment.objects.filter(post_id=post_id).update(status=status)
    return JsonResponse({'comment': 'Changes made'})
