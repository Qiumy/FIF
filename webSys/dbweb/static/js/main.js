$("li.nav-hover")
    .mouseenter(function (event) {
        $(this).addClass("open");
    })
    .mouseleave(function (event) {
        $(this).removeClass("open");
    });


var placeholder = $("input.js-search").prop('placeholder')
$("input.js-search")
    .focus(function () {
        $(this).prop("placeholder", "").addClass("active");
    })
    .blur(function () {
        $(this).prop("placeholder", placeholder).removeClass("active");
    });

$("#language").on('change', function () {
    var e = document.getElementById("language");
    var code_mode = e.options[e.selectedIndex].value;
    var editor = ace.edit("editor");
    editor.getSession().setMode(code_mode);
});

function alert_modal(content, isHtml) {
    var obj = $("#modal-alert");
    if (isHtml) {
        obj.find(".modal-body").html(content);
    }
    else {
        obj.find(".modal-body").text(content);
    }
    obj.modal('show');
}

