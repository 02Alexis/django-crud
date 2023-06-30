// $(document).ready(function() {
//     $("#remove-item").on("click", removeItem);
// });

// function removeItem() {
//     // Obtenemos el último formulario de la tabla
//     var lastElement = $(".table tr:last");
//     // Obtenemos el total de formularios ya que ahora tenemos
//     // que descontar un formulario
//     var table = document.getElementById("form_table");
//     var total = table.rows.length;
    
//     $(lastElement).remove();
//     // Actualizamos el total de los formularios
//     total--;
//     console.log(total);
//     // Solo mostrar el botón si existe por lo menos un formulario
//     if (total < 3) {
//         $("#remove-item").hide();
//     }
// }