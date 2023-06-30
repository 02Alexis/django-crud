
  $('.delete_button').click(
    function(e){
      var result = confirm("¿Está seguro de que desea eliminar este campo? \n Esta opción no se puede deshacer");
      if(!result) {
          e.preventDefault();
      }
  });