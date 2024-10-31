$(document).ready(function () {
    $(".editModalButton").on("click", editModalAjax);
    $(".deleteModalButton").on("click", deleteModalAjax);
    $(".cpfcnpj").inputmask("999.999.999-99");
});

function changePartnerType() {
    const value = this.value
    if (value == "PF") {
        $(".cpfcnpj").inputmask("999.999.999-99");
    } else {
        $(".cpfcnpj").inputmask("99.999.999/9999-99");
    }
}

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
            $("#partnerCodeInput").val(res.partnerCode);
            $("#descriptionInput").val(res.description);
            $("#partnerTypeInput").val(res.partnerType);
            $("#nationalIdInput").val(res.nationalId);
            $("#addressInput").val(res.address);
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