import markdown
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

# Extensions used to render Markdown post bodies. "extra" covers fenced code
# blocks and tables; "smarty" produces curly quotes so Markdown posts match the
# typography of the older CKEditor ones.
MARKDOWN_EXTENSIONS = ["extra", "sane_lists", "smarty"]


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    body_md = models.TextField(
        blank=True,
        verbose_name="Body (Markdown)",
        help_text=(
            "Preferred for new posts. In Notion, select the post and press "
            "Cmd+Shift+C to copy clean Markdown, then paste it here. If this "
            "field has content it is used instead of the rich text Body above."
        ),
    )
    show_in_feed = models.BooleanField(default=True)
    note = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=128, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post", kwargs={"slug": self.slug})

    @property
    def body_html(self):
        """Render the post body, preferring Markdown over the legacy HTML.

        Existing posts only have `body` (CKEditor HTML) and keep rendering as
        they always have. New posts written in `body_md` are rendered here.
        """
        if self.body_md.strip():
            return mark_safe(
                markdown.markdown(self.body_md, extensions=MARKDOWN_EXTENSIONS)
            )
        return mark_safe(self.body or "")
