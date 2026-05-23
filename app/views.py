from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def sobre(request):
    return render(request, 'sobre.html')


def elenco(request):

    personagens = [
        {
            'nome': 'Sophie Hatter',
            'dublador': 'Patrícia Scalvi',
            'imagem': 'imgs/sophie.jpeg'
        },

        {
            'nome': 'Howl',
            'dublador': 'Marcelo Campos',
            'imagem': 'imgs/howl.jpeg'
        },
    ]

    return render(request, 'elenco.html', {
        'personagens': personagens
    })
def elenco(request):
    return render(request, 'elenco.html')