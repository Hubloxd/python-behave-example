from django.shortcuts import render


# Create your views here.
def blackjack(request):
    return render(request, 'blackjack.html')
