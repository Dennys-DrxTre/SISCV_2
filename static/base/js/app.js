function submit_detail(url, parameters, callback) {
  $.ajax({
    url: url, //window.location.pathname
    type: "POST",
    data: parameters,
    dataType: "json",
    processData: false,
    contentType: false,
  })
    .done(function (data) {
      if (!data.hasOwnProperty("error")) {
        callback(data);
        return false;
      }
      message_error(data.error);
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      alert(textStatus + ": " + errorThrown);
    })
    .always(function (data) {});
}

function submit_with_ajax(url, title, content, parameters, callback) {
  $.confirm({
    theme: "bootstrap",
    title: title,
    icon: "fa fa-info",
    content: content,
    columnClass: "small",
    typeAnimated: true,
    cancelButtonClass: "btn-primary",
    draggable: true,
    dragWindowBorder: false,
    buttons: {
      info: {
        text: "Si",
        btnClass: "btn-dark",
        action: function () {
          $.ajax({
            url: url, //window.location.pathname
            type: "POST",
            data: parameters,
            dataType: "json",
            processData: false,
            contentType: false,
          })
            .done(function (data) {
              if (!data.hasOwnProperty("error")) {
                callback();
                return false;
              }
              message_error(data.error);
            })
            .fail(function (jqXHR, textStatus, errorThrown) {
              alert(textStatus + ": " + errorThrown);
            })
            .always(function (data) {});
        },
      },
      danger: {
        text: "No",
        btnClass: "btn-red",
        action: function () {},
      },
    },
  });
}

$(function () {
  $('a[rel="read"]').on("click", function () {
    var parameters = new FormData();
    parameters.append("action", "read");
    parameters.append("id", $(this).attr("id"));
    $(this).remove();
    submit_detail('/', parameters, function () {
    });
  });
});
