from django.shortcuts import render

def index(request):
    from .forms import ContactForm  # Move this import inside the function
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle successful form submission (e.g., send email, save data, etc.)
            return render(request, 'home/index.html', {'form': form, 'success': 'Your message has been sent!'})
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {'form': form})
