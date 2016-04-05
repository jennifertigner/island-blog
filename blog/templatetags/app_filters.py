from django import template

register = template.Library()

@register.filter()
def get_number_comments(articleID):
    num_comments = 0
    for comment in all_comments:
        if comment.article == articleID:
            num_comments += 1
    return num_comments
