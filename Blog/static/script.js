// These functions basically embedds soundcloud links
document.addEventListener("DOMContentLoaded", function(event) {
    (function ($) {
        $.fn.scembed = function(){
        var datasource  = 'http://soundcloud.com/oembed';
        return this.each(function () {
            var container = $(this);
            var mediasource = $(container).attr("sc_url");
            var params = 'url=' + mediasource + '&format=json&iframe=true&maxwidth=480&maxheight=120&auto_play=false&show_comments=false';
            $.ajaxopts = $.extend($.ajaxopts, {
                                url: datasource,
                                data: params,
                                dataType: 'json',
                                success: function (data, status, raw) {
                                    $(container).html(data.html);
                                },
                                error: function (data, e1, e2) {
                                    $(container).html("Can't retrieve player for " + mediasource);
                                },
                            });
            $.ajax($.ajaxopts);
            });
        };
    })(jQuery);

    $(function(){
        $("div.soundcloudEmbed").scembed();
    });
});
