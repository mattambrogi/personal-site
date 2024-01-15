from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse

class MostRecentPostsFeed(Feed):
    title = 'Matt Ambrogi'
    link = ''
    description = 'Most recent posts'

    def items(self):
        return Post.objects.all().filter(show_in_feed=True).order_by('created_at')
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)
    