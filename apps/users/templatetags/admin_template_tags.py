from django import template

register = template.Library()


@register.filter(name="is_superuser")
def example_filter(userqueryset, bool_value):
    result = []
    for user in userqueryset:
        result.append(user) if user.is_superuser is bool_value else None
    return result
