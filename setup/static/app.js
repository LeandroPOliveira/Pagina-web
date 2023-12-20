$('form input[type="file"]').change(event => {
  let arquivos = event.target.files;
  if (arquivos.length === 0) {
    console.log('sem imagem pra mostrar')
  } else {
      if(arquivos[0].type == 'image/jpeg') {
        $('img').remove();
        let imagem = $('<img class="img-fluid">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
        $('figure').prepend(imagem);
      } else {
        alert('Formato não suportado')
      }
  }
});

$(document).on('click', '#add-cart', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "cart_add" %}',
        data: {
            product_id: $('#add-cart').val()},
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
    },
    success: function(json){
    console.log(json)
    },
    error: function(xhr, errmsg, err){
    }
    });
})