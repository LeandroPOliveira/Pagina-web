from django.shortcuts import render


def pagamento_sucesso(request):

    return render(request, 'pagamento_sucesso.html', {})
