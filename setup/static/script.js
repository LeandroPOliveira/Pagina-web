$(document).on('click', '#add-cart', function(e){
    console.log('Click event triggered');
    e.preventDefault();

    // Get the URL from the data attribute
    var addUrl = $(this).data('add-url');

    $.ajax({
        type: 'POST',
        url: addUrl,
        data: {
            product_id: $(this).val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },
        success: function(json){
            console.log(json);
            document.getElementById("cart_quantity").textContent = json.qty;
        },
        error: function(xhr, errmsg, err){
            // Handle error
        }
    });
});


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

