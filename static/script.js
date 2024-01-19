$(document).on('click', '#add-cart', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url 'cart_adicionar' %}',
        data: {
    product_id: $('#add-cart').val(),
    product_qty: $('#qty-cart option:selected').text(),
    csrfmiddlewaretoken: '{{ csrf_token }}',
    action: 'post'
        },

        success: function(json){
            //console.log(json)
            document.getElementById("cart_quantity").textContent = json.qty
            location.reload();
        },

        error: function(xhr, errmsg, err){

        }


    });



})



const root = document.documentElement;
const marqueeElementsDisplayed = getComputedStyle(root).getPropertyValue("--marquee-elements-displayed");
const marqueeContent = document.querySelector("ul.marquee-content");

root.style.setProperty("--marquee-elements", marqueeContent.children.length);

for(let i=0; i<marqueeElementsDisplayed; i++) {
  marqueeContent.appendChild(marqueeContent.children[i].cloneNode(true));
}

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

