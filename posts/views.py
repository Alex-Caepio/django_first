from django.http import JsonResponse
from django.shortcuts import render

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


def my_posts(request):
    all_posts = []

    for post in POSTS:
        all_posts.append(post)

    # Return all_posts as a JSON response
    return JsonResponse(all_posts, safe=False)
