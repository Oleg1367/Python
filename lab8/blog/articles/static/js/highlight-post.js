$(document).ready(function(){
    $('.one-post').hover(function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 300);
    }, function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
    })
    
    $('.header').hover(function(event){
        $(event.currentTarget).find('img').animate({width: '338px'}, 300);
    }, function(event){
        $(event.currentTarget).find('img').animate({width: '318px'}, 300);
    })
});