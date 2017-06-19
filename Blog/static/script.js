/* JAVASCRIPT FOR: Blog/templates/blog/index.html */

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
//Takes the a Youtube URL and retreives the so called Id
function getId(url) {
  var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
  var match = url.match(regExp)
  if (match && match[2].length == 11) {
      return match[2]
  } else {
      return 'error'
  }
}
//Generates HTML code based on the Id from the getId()-function and then adds the HTML to the div surrounding this <script>
//The id-argument tells the function exactly which <div> it should add the HTML-code to, since all this code is inside a forloop it needs a specific ID which is the Primary Key of the current Post-object.
function youtubeEmbedder(url, id, tag) {
  var videoId = getId(url)
  $(tag + id).html('<iframe width="300" height="115" src="//www.youtube.com/embed/' + videoId + '" frameborder="0" allowfullscreen></iframe>')
}
