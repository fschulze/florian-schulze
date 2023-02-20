require('normalize.css');

document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelectorAll('.timestamp').forEach(element => {
        var time = new Date(element.textContent);
        if (isNaN(time)) {
            return;
        }
        time = new Date(Date.UTC(
            time.getFullYear(), time.getMonth(), time.getDate(),
            time.getHours(), time.getMinutes(), time.getSeconds()));
        var iso = time.toISOString();
        element.textContent = iso.slice(0, 10);
        element.setAttribute("title", iso);
    });
});
