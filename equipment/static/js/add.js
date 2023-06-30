$(document).ready(function() {
    $("#add-item").on("click", addItem);
});

function addItem() {
    // Clonamos la ultima fila de la tabla
    var newElement = $(".table tr:last").clone(true);
    // Necesitamos aumentar en 1 el total de los formularios
    // por eso obtenemos el total actual, debería ser 4
    var table = document.getElementById("form_table");
    var total = table.rows.length;
    
    // Cuando se usan formsets, los elementos del formulario 
    // son enumerados (id_item-0-rate, id_item-1-rate, etc.)              
    // entonces necesitamos que el nuevo elemento siga esa 
    // numeración
    newElement.find(":input").each(function() {
        var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
        var id = "id_" + name;
        // Seteamos los atributos y limpiamos los valores
        $(this).attr({"name": name, "id": id}).val("");
    });
    // Aumentamos en 1 la cantidad de formularios en el formset
    total++;
    console.log(total);

    // Insertamos el nueva formulario al final
    $(".table tr:last").after(newElement);
    // Solo mostramos el botón para quitar si hay mas de un formulario
    if (total >= 3) {
        $("#remove-item").show();
    }
}