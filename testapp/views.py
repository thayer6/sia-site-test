
from django.shortcuts import render
from testapp.models import Text
from django.shortcuts import HttpResponse
# Create your views here.

def appview(request):
    if request.method == "POST":
        search_id = request.POST.get('textfield', None)
        #html = ("<h1>%s</h1>", search_id)

        Text.objects.create(
            searched_text = search_id,
        )

    return render(request, 'app_page.html')
