from django import template

register = template.Library()

@register.filter(name='clean_event')
def clean_event(value):
    """
    Converts GitHub Event types (PushEvent) into readable text.
    """
    mapping = {
        'PushEvent': 'Pushed to',
        'CreateEvent': 'Created',
        'WatchEvent': 'Starred',
        'IssuesEvent': 'Opened issue in',
        'PullRequestEvent': 'PR in',
        'ForkEvent': 'Forked',
    }
    # Return the mapped value, or the original if not found (minus "Event")
    return mapping.get(value, value.replace('Event', ''))