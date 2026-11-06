from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'interaction/success.html', {'data': data})
    else:
        form = ContactForm()
    return render(request, 'interaction/contact_form.html', {'form': form})
