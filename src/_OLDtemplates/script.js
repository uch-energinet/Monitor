var side_panels = document.getElementsByClassName("side-panel");

function show_or_hide_content(content, header, max_height) {
    return function () {
        if (content.style.maxHeight) {
            content.style.maxHeight  = null;
            header.style.borderRadius = "10px";
        } else {
            content.style.maxHeight = max_height + "px";
            header.style.borderRadius = "10px 10px 0 0";
        }
    }
}

function open_side_panel(side_panel) {
    return function () {
        if (side_panel.classList.contains("open")) {
            side_panel.classList.remove("open")
        } else {
            side_panel.classList.add("open")
        }
    }
}

for (let i=0; i < side_panels.length; i++) {
    var side_panel = side_panels[i];
    var header = side_panel.getElementsByClassName("side-panel-header")[0];
    var content = side_panel.getElementsByClassName("side-panel-content")[0];
    var commands = content.getElementsByTagName("p")
    var max_height = 0;
    for (let j=0; j < commands.length; j++) {
        max_height += commands[i].clientHeight;
    }
    header.addEventListener("click", open_side_panel(side_panel))
}