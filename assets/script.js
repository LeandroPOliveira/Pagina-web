let tempo = 2000,
    currentImageIndex = 0,
    marcas = document.querySelectorAll('.marcas__imagem')
max = marcas.length;

function proximaImagem() {

    marcas[currentImageIndex].classList.remove('selecionada')

    currentImageIndex++

    if (currentImageIndex >= max) {
        currentImageIndex = 0
    }

    marcas[currentImageIndex].classList.add('selecionada')
}

function start() {
    setInterval(() => {
        proximaImagem()
    }, tempo)
}

window.addEventListener('load', start)