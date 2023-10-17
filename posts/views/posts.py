from django.db import transaction
from django.http import JsonResponse
from django.views import View

from posts.models import Post, Comment
import json


class PostView(View):
    def get(self, request):
        result = []
        posts = Post.objects.all().filter(id__gt=0).order_by('-id')
        for post in posts:
            result.append({'id': post.id, 'title': post.title, 'text': post.text})

        return JsonResponse({'posts': result})

    def post(self, request):
        title = json.loads(request.body.decode('utf-8')).get('title', '')
        text = json.loads(request.body.decode('utf-8')).get('text', '')
        category = json.loads(request.body.decode('utf-8')).get('category', '')

        with transaction.atomic():
            new_post = Post(title=title, text=text, category=category)
            new_comment = Comment(post=new_post, text='comment', status='created')
            new_post.save()
            new_comment.save()

        return JsonResponse(
            {'id': new_post.id, 'title': new_post.title, 'text': new_post.text, 'category': new_post.category,
             'created_at': new_post.created_at, 'comment': new_comment.text, 'status': new_comment.status},
            status=201)


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
