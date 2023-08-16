document.getElementById("metodoForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var selectedValue = document.getElementById("Metodos").value;

    if (selectedValue === "Post") {
        var newForm = document.createElement("form");
        newForm.action = "/agregarCategoria";
        newForm.method = "post";

        var nombreLabel = document.createElement("label");
        nombreLabel.textContent = "Nombre:";
        var nombreInput = document.createElement("input");
        nombreInput.type = "text";
        nombreInput.id = "nombre";
        nombreInput.name = "nombre";
        nombreInput.required = true;
        newForm.appendChild(nombreLabel);
        newForm.appendChild(nombreInput);
        newForm.appendChild(document.createElement("br"));

        var descripcionLabel = document.createElement("label");
        descripcionLabel.textContent = "Descripción:";
        var descripcionInput = document.createElement("input");
        descripcionInput.type = "text";
        descripcionInput.id = "descripcion";
        descripcionInput.name = "descripcion";
        descripcionInput.required = true;
        newForm.appendChild(descripcionLabel);
        newForm.appendChild(descripcionInput);
        newForm.appendChild(document.createElement("br"));

        
        var submitButton = document.createElement("input");
        submitButton.type = "submit";
        submitButton.value = "Agregar";
        newForm.appendChild(submitButton);
        document.body.appendChild(newForm);
    }
});