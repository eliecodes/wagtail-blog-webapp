from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from taggit.models import Tag as TaggitTag, TaggedItemBase
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.tags import ClusterTaggableManager



class Blogpage(Page):
    description = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

class PostPage (Page):
    header_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL , related_name="+")
    tags = ClusterTaggableManager(through= "PostPageTags", blank=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("tags"),
        
        InlinePanel("categories", label="category"),
    ]




class PostPageBlogCategory(models.Model):
    page = ParentalKey("blog.PostPage", on_delete=models.CASCADE, blank=True, related_name="categories" )
    blog_category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE, related_name="post_page"  )

    panels = [
        SnippetChooserPanel("blog_category"),
    ]
    class Meta:
        unique_together = ("page","blog_category")

class PostPageTags(TaggedItemBase):
    content_object = ParentalKey("PostPage", blank=True, related_name="post_tags" )

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=80, unique=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name ="Category"
        verbose_name_plural ="Categorie"

    def __str__(self):
        return self.name
# @register_snippet
# class Tag(TaggitTag):
#     class Meta:
#         proxy = True