$(function(){
  if($('main').is('.teste1')){
    const root = document.documentElement;
    const marqueeElementsDisplayed = getComputedStyle(root).getPropertyValue("--marquee-elements-displayed");
    const marqueeContent = document.querySelector("ul.marquee-content");

    root.style.setProperty("--marquee-elements", marqueeContent.children.length);


    for(let i=0; i<marqueeElementsDisplayed; i++) {
    marqueeContent.appendChild(marqueeContent.children[i].cloneNode(true));
}

  }
});

setTimeout(() => {
  document.querySelector('#alerta').style.display = 'none'
}, 5000)



function previewImage(input) {
    var preview = document.getElementById('foto-preview');
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        preview.src = "#";
    }
}

document.querySelector('nav-link').onclick = function(e) {
    e.preventDefault();
    console.log('teste')
    var href = document.querySelector('#teste').href;
    window.location = href;
}