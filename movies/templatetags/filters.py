
from django import template

register = template.Library()

@register.filter
def display_rating(rating_count):
    html = ''
    
    for i in range(int(rating_count)):
        html += '<i class="fa fa-star active"></i>'
    for i in range(5-int(rating_count)):
        html += '<i class="fa fa-star"></i>'


    return html