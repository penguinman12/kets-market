
from django import template

register = template.Library()
@register.filter
def calculate_percentage(user, latest_price):
    carbon_credits = user.account.carbon_credits
    cash = user.account.cash
    percentage = (carbon_credits * latest_price + cash - 5535500) / 5535500 * 100
    return round(percentage, 3)