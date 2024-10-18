$(document).ready(function () {
    $(".editModalButton").on("click", editModalAjax);
    $(".deleteModalButton").on("click", deleteModalAjax);
});

function editModalAjax() {
    $.ajax({
        url: "get-rowData/",
        type: "POST",
        data: JSON.stringify({
            objectId: $(this).closest("span").data("id")
        }),
        dataType: "json",
        success: function (res, status) {
            $("#objectIdInput").val(res.id);
            $("#dateStartInput").val(res.dateStart);
            $("#dateEndInput").val(res.dateEnd);
            $("#activityInput").val(res.activity);
            $("#descriptionInput").val(res.description);
        },
        error: function (res) {
            alert(res.status);
        }
    });
};

function deleteModalAjax() {
    $.ajax({
        url: "get-rowData/",
        type: "POST",
        data: JSON.stringify({
            objectId: $(this).closest("span").data("id")
        }),
        dataType: "json",
        success: function (res, status) {
            $("#objectIdDelete").val(res.id);
        },
        error: function (res) {
            alert(res.status);
        }
    });
};