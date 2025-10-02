from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for VISITING!"
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
    
class ProductsView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {"name": "Product 1", "price": "$10", "description": "Product #1 description."},
            {"name": "Product 2", "price": "$20", "description": "Product #2 description."},
            {"name": "Product 3", "price": "$30", "description": "Product #3 description."},
            {"name": "Product 4", "price": "$40", "description": "Product #4 description."},
        ]
        return context