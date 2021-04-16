
from django.shortcuts import render
from testapp.models import Text
from django.shortcuts import HttpResponse
from reportlab.pdfgen.canvas import Canvas
from fpdf import FPDF
# Create your views here.

def appview(request):
    if request.method == "POST":
        search_id = request.POST.get('textfield', None)
        #html = ("<h1>%s</h1>", search_id)

        Text.objects.create(
            searched_text = search_id,
        )

    return render(request, 'app_page.html')

def report(request):
    class PDF(FPDF):
        pass # nothing happens when it is executed.
    pdf = PDF()#pdf 
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'My second(?) PDF!')
    pdf.output('report.pdf', 'F')

    with open('./report.pdf', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s' % 'report.pdf'
    return response

def zip(request):

    zip_file = open('testapp/static/pdfs.zip', 'rb')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'pdfs.zip'

    return response