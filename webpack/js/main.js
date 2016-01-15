var moment = require('moment');
require('normalize.css');
require('jquery.cookie');
require('../SocialSharePrivacy/javascripts/socialshareprivacy.js');
require('../SocialSharePrivacy/javascripts/modules/buffer.js');
require('../SocialSharePrivacy/javascripts/modules/delicious.js');
require('../SocialSharePrivacy/javascripts/modules/disqus.js');
require('../SocialSharePrivacy/javascripts/modules/facebook.js');
require('../SocialSharePrivacy/javascripts/modules/gplus.js');
require('../SocialSharePrivacy/javascripts/modules/hackernews.js');
require('../SocialSharePrivacy/javascripts/modules/linkedin.js');
require('../SocialSharePrivacy/javascripts/modules/pinterest.js');
require('../SocialSharePrivacy/javascripts/modules/reddit.js');
require('../SocialSharePrivacy/javascripts/modules/stumbleupon.js');
require('../SocialSharePrivacy/javascripts/modules/tumblr.js');
require('../SocialSharePrivacy/javascripts/modules/twitter.js');
require('../SocialSharePrivacy/javascripts/modules/xing.js');

$(function() {
    $.fn.socialSharePrivacy.settings.path_prefix = "/";
    $.fn.socialSharePrivacy.settings.css_path = "";
    $.fn.socialSharePrivacy.settings.order = [
        "facebook", "twitter", "gplus", "linkedin", "xing", "reddit", "pinterest", "disqus"];
    $.fn.socialSharePrivacy.settings.services.twitter.via = "fschulze";
    $('*[data-social-share-privacy=true]:not([data-init=true])').
      socialSharePrivacy().attr('data-init', 'true');

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
