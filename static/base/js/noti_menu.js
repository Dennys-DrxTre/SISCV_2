let tblCate;
let modal_title;
let messages;

/** TABLE NOTIFICATIONS */
function getData() {
    tblCate = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        ordering:  false,
        destroy: true,
        deferRender: true,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "<span class='fa fa-angle-double-left'></span>",
                "sLast": "<span class='fa fa-angle-double-right'></span>",
                "sNext": "<span class='fa fa-angle-right'></span>",
                "sPrevious": "<span class='fa fa-angle-left'></span>"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_all'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "unread"},
            {"data": "level"},
            {"data": "verb"},
            {"data": "description"},
            {"data": "timestamp"},
            {"data": "unread"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a href="#" rel="one_delete" class="btn btn-secondary mr-2"><i class="fas fa-trash"></i></a>';
                    if (data == 'No leido') {
                        buttons += '<a href="#" rel="one_read" class="btn btn-dark"><i class="fas fa-envelope-open"></i></a>';
                    }
                    return buttons;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (data == 'CONSULTA') {
                        data = `<span class="badge badge-secondary">${data}</span>`;
                    }else if(data == 'VACUNACIÓN'){
                        data = `<span class="badge badge-dark">${data}</span>`;
                    }else if(data == 'DESPARASITACIÓN'){
                        data = `<span class="badge badge-warning">${data}</span>`;
                    }
                    return data;
                }
            },
        ],
        initComplete: function (settings, json) {
            
        }
    });
}


$(function () {

    getData();
    /** all read */
    $('a[rel="read_all_btn"]').on("click", function () {
        var parameters = new FormData();
        parameters.append("action", "all_read");
        submit_with_ajax(window.location.pathname,'Notifiación', '¿Estas seguro de marcar todas las notificaciones como leidas?', parameters, function () {
            tblCate.ajax.reload();
            toastr.success('Acción realizada correctamente');
        });
    });

    /** one read */
    $('#data tbody').on('click', 'a[rel="one_read"]', function () {
        
        var tr = tblCate.cell($(this).closest('td, li')).index();
        var data = tblCate.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'one_read')
        parameters.append('id', data.id)
        submit_detail(window.location.pathname, parameters, function () {
            tblCate.ajax.reload();
            toastr.success('Acción realizada correctamente');
        });
    });

    /** one delete */
    $('#data tbody').on('click', 'a[rel="one_delete"]', function () {
        
        var tr = tblCate.cell($(this).closest('td, li')).index();
        var data = tblCate.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action', 'one_delete')
        parameters.append('id', data.id)
        submit_with_ajax(window.location.pathname,'Notifiación', '¿Estas seguro de eliminar esta notificación?', parameters, function () {
            tblCate.ajax.reload();
            toastr.success('Acción realizada correctamente');
        });
    });

    /** all delete */
    $('a[rel="all_delete"]').on("click", function () {
        var parameters = new FormData();
        parameters.append('action', 'all_delete')
        submit_with_ajax(window.location.pathname,'Notifiación', '¿Estas seguro de eliminar todas las notificaciones?', parameters, function () {
            tblCate.ajax.reload();
            toastr.success('Acción realizada correctamente');
        });
    });

});