let tempo = 2000,
    currentImageIndex = 0,
    marcas = document.querySelectorAll('.marcas__imagem')
max = marcas.length;

function proximaImagem() {

    
    marcas[currentImageIndex].style.left + 5 + 'px'

    currentImageIndex++

    if (currentImageIndex >= max) {
        currentImageIndex = 0
    }

    
}

function start() {
    setInterval(() => {
        proximaImagem()
    }, tempo)
}

window.addEventListener('load', start)