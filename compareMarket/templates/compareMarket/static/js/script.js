function filtro(){
  var caja = document.getElementById("busqueda");
  var prueba = document.getElementById("desplegar");
  var frase = document.getElementById("description");

  if(caja.checked==true){
      prueba.style.display="block";
      frase.style.display="none";

  } else{
      prueba.style.display="none";
      frase.style.display="block";
  }
}

function loading() {
    if (document.getElementById('leer').value != "")
    {
        var carga = document.getElementById("carga");
        carga.style.display = "flex";

        var newPageTitle = 'Comparando - Comparador de productos de supermercado';
        document.title = newPageTitle;
    }
}