from django.http import HttpResponse

class StripeWH_handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic /unknown/unexpected webhook event

        """
        return HttpResponse(
            content=f'webhook receiveed: {event["type"]}',
            status=200)