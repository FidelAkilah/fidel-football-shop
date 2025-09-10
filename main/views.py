from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406358636',
        'name': 'Fidel Akilah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)