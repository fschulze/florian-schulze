var moment = require('moment-mini');
require('normalize.css');

$(function() {
    moment.locale("en")
    moment.locale("en", {
        longDateFormat: {
            LT: "HH:mm",
            L: "YYYY-MM-DD"
        }
    });
    $('.timestamp').each(function() {
        var element = $(this);
        var time = moment.utc(element.text(), "YYYY-MM-DD HH:mm:ss");
        if (time.isValid()) {
            element.text(time.local().calendar());
            element.attr("title", time.local().toISOString());
        }
    });
});
