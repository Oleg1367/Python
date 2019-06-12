$(document).ready(function(){
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $topLogo = $('.logo');
    $(window).scroll(function() {
        // код, который нужно выполнять при
        // каждой прокрутке
        scrolled = $(window).scrollTop(); // Обновление значения текущей прокрутки
        for (var i = 0; i < $parallaxElements.length; i++){
            yPosition = (scrolled * 0.15*(i + 1));
            $parallaxElements.eq(i).css({ top: yPosition });
        }
        yPosition = scrolled;
        $topLogo.css({top: 0.8*yPosition});
    });
});