from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary using a key."""
    return dictionary.get(key)

@register.filter
def get_options(question):
    """Get question options as a list of tuples (option_num, option_text)."""
    return [
        ('1', question.option1),
        ('2', question.option2),
        ('3', question.option3),
        ('4', question.option4),
    ]
