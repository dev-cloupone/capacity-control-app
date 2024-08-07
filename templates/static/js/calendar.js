let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();
let pageLoad = true;
let selectedDay = 0;
let selectedMonth = 0;
let selectedYear = 0;

 
const day = document.querySelector(".calendar-dates");
 
const currdate = document
    .querySelector(".calendar-current-date");
 
const prenexIcons = document
    .querySelectorAll(".calendar-navigation span");
    
 
// Array of month names
const months = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
];
 
// Function to generate the calendar
const manipulate = () => {
 
    // Get the first day of the month
    let dayone = new Date(year, month, 1).getDay();
 
    // Get the last date of the month
    let lastdate = new Date(year, month + 1, 0).getDate();
 
    // Get the day of the last date of the month
    let dayend = new Date(year, month, lastdate).getDay();
 
    // Get the last date of the previous month
    let monthlastdate = new Date(year, month, 0).getDate();
 
    // Variable to store the generated calendar HTML
    let lit = "";
 
    // Loop to add the last dates of the previous month
    for (let i = dayone; i > 0; i--) {
        lit +=
            `<li class="inactive">${monthlastdate - i + 1}</li>`;
    }
 
    // Loop to add the dates of the current month
    for (let i = 1; i <= lastdate; i++) {
 
        let isToday = false;
        // Check if the current date is today
        if(pageLoad) {
            isToday = i === date.getDate()
            && month === new Date().getMonth()
            && year === new Date().getFullYear()
            ? "active"
            : "";
        } else {
            isToday = i === selectedDay 
            && month === selectedMonth
            && year === selectedYear
            ? "active" : "";
        }
        if(isToday !== "") {
            const dateMonth = month + 1
            $("#insertDateInput").val(year + "-" + dateMonth + "-" + i)
        }
        lit += `<li data-day="${i}" data-month="${month}" data-year="${year}" class="${isToday} monthDay">${i}</li>`;
    }
 
    // Loop to add the first dates of the next month
    for (let i = dayend; i < 6; i++) {
        lit += `<li class="inactive">${i - dayend + 1}</li>`
    }
 
    // Update the text of the current date element 
    // with the formatted current month and year
    currdate.innerText = `${months[month]} ${year}`;
 
    // update the HTML of the dates element 
    // with the generated calendar
    day.innerHTML = lit;
    pageLoad = false;
}
 
manipulate();
 
// Attach a click event listener to each icon
prenexIcons.forEach(icon => {
 
    // When an icon is clicked
    icon.addEventListener("click", () => {
 
        // Check if the icon is "calendar-prev"
        // or "calendar-next"
        month = icon.id === "calendar-prev" ? month - 1 : month + 1;
 
        // Check if the month is out of range
        if (month < 0 || month > 11) {
 
            // Set the date to the first day of the 
            // month with the new year
            date = new Date(year, month, new Date().getDate());
 
            // Set the year to the new year
            year = date.getFullYear();
 
            // Set the month to the new month
            month = date.getMonth();
        }
 
        else {
 
            // Set the date to the current date
            date = new Date();
        }
 
        // Call the manipulate function to 
        // update the calendar display
        manipulate();
    });
});

$(document).ready(function () {
    $("body").on("click", ".monthDay", function () {
        selectedDay = $(this).data("day");
        selectedMonth = parseInt($(this).data("month"));
        selectedYear = $(this).data("year");
        manipulate();
        $.ajax({
            url: "get-dayFilterData/",
            type: "POST",
            data: JSON.stringify({
                day: selectedDay,
                month:  selectedMonth + 1,
                year: selectedYear
            }),
            dataType: "json",
            success: function (res, status) {
                $(".todayList").css("display","none");
                $("#activitiesBody").empty();
                $.each(res, function(index, item) {
                    let newRow = $('<tr id="' + item.pk + '" class="todayList"></tr>');
                    const delimiter = ":";
                    newRow.append($('<td class="dateStartField" style="color: #07698c; width: 10%;"></td>').text(item.fields.dateStart.split(delimiter).slice(0, 2).join(delimiter))); 
                    newRow.append($('<td class="dateEndField" style="color: #07698c; width: 10%;"></td>').text(item.fields.dateEnd.split(delimiter).slice(0, 2).join(delimiter))); 
                    newRow.append($('<td class="activityField" style="color: #07698c; width: 28%;"></td>').text(item.fields.activity)); 
                    newRow.append($('<td class="descriptionField" style="color: #07698c; width: 28%;"></td>').text(item.fields.description)); 
                    newRow.append($('<td style="color: #07698c; width: 6%;"></td>').text(item.fields.total)); 
                    newRow.append($('<td style="width: 10%; min-width: 10%; text-align: right"><a type="button" data-toggle="modal" data-id="' + item.pk + '"' +
                  'data-target="#editModal"><span id="calendar-next" data-id="' + item.pk + '" class="material-symbols-rounded editModalButton">' +
                    'edit' +
                  '</span></a></td>'));
                  newRow.append($('<td style="width: 10%; min-width: 10%; text-align: right"><a type="button" data-toggle="modal"' +
                  'data-target="#deleteModal' + item.pk + '"><span id="calendar-next" class="material-symbols-rounded">' +
                    'delete' +
                  '</span></a></td>')); 
                        
                    $('#activitiesBody').append(newRow);
                    $('.deleteModalButton').on("click", deleteModalAjax);
                    $('.editModalButton').on("click", editModalAjax);
                });

            },
            error: function (res) {
                alert(res.status);
            }
        });
    })
});