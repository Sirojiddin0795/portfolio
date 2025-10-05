from .models import HomePageContent

def home_content_processor(request):
    home_content = HomePageContent.objects.first()
    return {'home_content': home_content}
