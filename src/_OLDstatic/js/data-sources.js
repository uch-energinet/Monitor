$(document).ready(function(){
    var socket = io();
    socket.on('connect', function() {
        socket.emit("connected")
    });
    processElem = $(".process").first()
    socket.on('message', function(data) {
        processElem.append(data.data + "<br>")
    })
    socket.on('redirect', function(data) {
        window.open("www.google.dk")
    })
});

console.log("opening google")
window.open("https://www.google.dk", "_blank")



$(".task").each(function() {
    var task = $(this)
    var header = task.find(".header").eq(0);
    var content = task.find(".content").eq(0);
    var hiddenSymbol = header.find(".hidden-symbol").eq(0)
    header.on("click", function() {
        if (task.hasClass("hidden")) {
            task.removeClass("hidden")
            hiddenSymbol.html("−")
        } else {
            task.addClass("hidden")
            hiddenSymbol.html("+")

        }
    })
})

$(".do").each(function() {
    console.log($(this))
    $(this).on("click", function() {
        $.getJSON("start-job")
    })
})