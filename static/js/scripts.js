document.addEventListener('submit', async function (e) {
    const nombre = document.getElementById('nombre').value.trim();
    const telefono = document.getElementById('telefono').value.trim();
    console.log('Nombre:', nombre);
    console.log('Teléfono:', telefono);

    const resp = await fetch('/flex', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body
    });


    // Aquí puedes agregar la lógica para enviar los datos al servidor si es necesario
});