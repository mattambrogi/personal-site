import html

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.html import strip_tags
from .models import Post

class MostRecentPostsFeed(Feed):
    title = 'Matt Ambrogi'
    link = ''
    description = 'Most recent posts'

    def items(self):
        return Post.objects.all().filter(show_in_feed=True).order_by('created_at')
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # body_html covers both Markdown and legacy CKEditor posts. Strip tags
        # for a plain-text excerpt, then unescape so CKEditor's encoded
        # entities (&quot;, &rsquo;) don't get double-escaped by the feed.
        return truncatewords(html.unescape(strip_tags(item.body_html)), 20)
