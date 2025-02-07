let dataTable;
let tableIsInitialized = false;

const tableOptions = {
    columnDefs: [
        { className:"dt-center", targets: "_all" },
        { searchable: false, targets: [0, 4] }
    ],
    pageLength: 4,
    destroy: true
};

const initTable = async() => {

    if (tableIsInitialized) {
        dataTable.destroy();
    }
    await listTransaccion();

    dataTable = $("#tableTransaccions").DataTable(tableOptions);

    tableIsInitialized = true;
}

const listTransaccion = async() => {
    
    try {

        const response = await fetch('http://localhost:8000/app/accountsJSON/');
        const data = await response.json();

        document.getElementById("tableBodyTransaccions").innerHTML = ``;
            
        data.historialTransacciones.forEach((historialTransacciones, index) => {
            const tr = document.createElement("tr");

            tr.appendChild(createTagWithOptions("td", { innerText: index + 1 }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.numeroDeCuenta }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.numeroComprobante }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.tipoDeComprobante }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.descripcion }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.debito }));
            tr.appendChild(createTagWithOptions("td", { innerText: historialTransacciones.credito }));

            document.getElementById("tableBodyTransaccions").appendChild(tr);
        });

    } catch(ex) {
        alert(ex);
    }
}

function createTagWithOptions(tag, options) {
    const element = document.createElement(tag);
    Object.assign(element, options);
    return element;
}

window.addEventListener('load', async() => {
    await initTable();
})