import json

from django.http import JsonResponse
from django.views import View

from posts.models import Post


class DetailedPost(View):
    @staticmethod
    def parse_post(post: Post):
        return {
            'id': post.id,
            'title': post.title,
            'text': post.text,
            'category': post.category,
        }

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return JsonResponse({'post': self.parse_post(post)})

    def put(self, request, post_id):
        post = Post.objects.get(id=post_id)
        data = json.loads(request.body.decode('utf-8'))
        post.title = data.get('title', '')
        post.text = data.get('text', '')
        post.category = data.get('category', '')
        post.save()
        return JsonResponse({'post': self.parse_post(post)})

    def delete(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({'deleted': True})
