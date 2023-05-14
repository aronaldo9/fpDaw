// Añade un párrafo más a la caja article.
function añadir() {
    var nuevoP = document.createElement("p");
    var contenido = document.createTextNode("PÁRRAFO AÑADIDO: Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui repellendus culpa recusandae? Deserunt nam amet unde placeat, est tenetur nihil adipisci corrupti non fuga voluptatibus dicta explicabo aut. Hic, temporibus.");
    nuevoP.appendChild(contenido);
    var element = document.getElementById("articulo");
    element.appendChild(nuevoP);
}

// Elimina el elemento dos de section.
function eliminar() {
    var element = document.getElementById("p5");
    element.remove();
}

// Cambia el contenido del primer párrafo de article.
function cambiar() {
    document.getElementById("p1").innerHTML = "<p>El contenido de este párrafo ha sido cambiado</p>"
}

//  Modifica el color del texto de article.
function cambiarColor() {
    document.getElementById("articulo").style.color = "red";
}

// Añade un background a section.
function ponerFondo() {
    document.getElementById("seccion").style.backgroundColor = "aquamarine";
    document.getElementById("seccion").style.color= "darkred";
}

// Añade un borde a article.
function ponerBorde() {
    document.getElementById("articulo").style.border = "2px solid aquamarine";
    articulo.style.padding = "10px";
}