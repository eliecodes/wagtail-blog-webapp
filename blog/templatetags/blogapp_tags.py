from blog.models import Tag, BlogCategory
from django.template import Library


register = Library()


@register.inclusion_tag("components/main_categories.html", takes_context=True)
def category_list (context):
    categories = BlogCategory.objects.all()
    return {
        "request":context["request"],
        "categories":categories
    }

@register.inclusion_tag ("components/main_tags.html", takes_context=True)
def tag_list(context):
    tags = Tag.objects.all()
    return {
        "request":context["request"],
        "tags":tags
    }

@register.inclusion_tag("components/post_tags.html",takes_context=True)
def post_tag_list(context):
    page = context["page"]
    post_tags = page.tags.all()
    return {
        "request":context["request"],
        "post_tags":post_tags
    }

@register.inclusion_tag ("components/post_categories.html", takes_context=True)
def post_categories_list (context):
    page = context["page"]
    post_categories = page.categories.all()
    return {
        "request":context["request"],
        "post_categories":post_categories
    }