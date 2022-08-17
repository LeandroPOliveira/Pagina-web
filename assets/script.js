// slider
const slides = document.getElementsByClassName("slide"); // this selection is a live collection; any changes in DOM is updated in the variable unlike querySelectors


let currentSlideIndex = 0;
let lastSlideIndex = slides.length - 1;

// go to a slide;
function goToSlide(slideIndex) {
    [...slides].forEach((s, i) => {
        s.style.transform = `translateX(${100 * (i - slideIndex)}%)`
    })
    currentSlideIndex = slideIndex;
}
goToSlide(currentSlideIndex);

// make ready the next slide if current slide is the first or the last slide
function readyNextSlide() {
    // if currentSlide is the last slide, shift the first slide to the end
    if (currentSlideIndex === lastSlideIndex) {
        slides[lastSlideIndex].insertAdjacentElement("afterend", slides[0]);
        slides[lastSlideIndex].style.transform = `translateX(${100}%)`;
        currentSlideIndex--; //this is because current slide is now the second last slide
    }
    // if currentSlide is the first slide, shift the last slide to the beginning
    if (currentSlideIndex === 0) {
        slides[0].insertAdjacentElement("beforebegin", slides[lastSlideIndex]);
        slides[0].style.transform = `translateX(-${100}%)`;
        currentSlideIndex++; //this is because current slide is now the second slide
    }
}

// put the last slide in the beginning; ('if' condition is not necessary but providing if condition is future proof if user sets the initial slide to be shown as the last slide )
if (currentSlideIndex === lastSlideIndex || currentSlideIndex === 0) readyNextSlide();

// shift all slides left or right based on direction provided
function shiftSlides(direction) {
    direction ? currentSlideIndex++ : currentSlideIndex--
    if (currentSlideIndex === lastSlideIndex || currentSlideIndex === 0) readyNextSlide();
    goToSlide(currentSlideIndex);
}
tempo = 3000;

function start() {
    setInterval(() => {
        shiftSlides(null, 1)
    }, tempo)
}

window.addEventListener('load', start)




