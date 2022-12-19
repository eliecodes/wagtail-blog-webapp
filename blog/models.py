from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class Blogpage(Page):
    description = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]

class PostPage (Page):
    header_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL , related_name="+")
    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
    ]
