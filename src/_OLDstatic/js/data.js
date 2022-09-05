$(document).ready(function(){
    var socket = io();
    socket.on('connect', function() {
        socket.emit("connected")
        console.log("`connected` has been emitted")
    });
    processElem = $(".process").first()
    socket.on('message', function(data) {
        processElem.append(data.data + "<br>")
    })

});

$(".task").each(function() {
    var task = $(this)
    var header = task.find(".header").eq(0);
    var content = task.find(".content").eq(0);
    var hiddenSymbol = header.find(".hidden-symbol").eq(0)
    console.log(content)
    header.on("click", function() {
        if (task.hasClass("hidden")) {
            task.removeClass("hidden")
            hiddenSymbol.html("-")
        } else {
            task.addClass("hidden")
            hiddenSymbol.html("+")

        }
    })
})