$(function(){
    var $reasonDescriptions = $('.reason-description')
    $("#reason-list").iosSlider({
        snapToChildren: true,
        desktopClickDrag: true,
        infiniteSlider: true,
        navNextSelector: $('.reasons .button.next'),
        navPrevSelector: $('.reasons .button.prev'),
        autoSlide: true,
        autoSlideTimer: 8000,
        autoSlideTransTimer: 800,
        onSliderLoaded: slideContentLoaded,
        onSlideComplete: slideContentComplete
    })
    function slideContentLoaded(args) {
        $(args.sliderObject).find('.reason-number, .reason-name, .reason-read-more-link').attr('style', '');
        $(args.currentSlideObject).find('.reason-number, .reason-name, .reason-read-more-link')
            .css({left: 0})
            .animate({opacity: 1}, 1200, 'linear')
    }
    function slideContentComplete(args) {
        if(!args.slideChanged) return false;
        $(args.sliderObject).find('.reason-number, .reason-name, .reason-read-more-link').attr('style', '');
        $(args.currentSlideObject).find('.reason-number').animate({
            left: 0,
            opacity: 1
        }, 800, 'easeOutQuint')
        $(args.currentSlideObject).find('.reason-name').animate({
            left: 0,
            opacity: 1
        }, 800, 'easeOutQuint')
        $(args.currentSlideObject).find('.reason-read-more-link').animate({
            left: 0,
            opacity: 1
        }, 800, 'easeOutQuint')
    }
    $(window).resize(function(){
        $reasonDescriptions.each(function(){
            var $this = $(this),
                thisHeight = $this.height(),
                parentHeight = $this.parent().height()
            if(parentHeight>thisHeight){
                $this.css({marginTop:(parentHeight-thisHeight)/2})
            } else {
                $this.css({marginTop:0})
            }
        })
    })
    $(window).resize()
    $(".reason-read-more-link").click(function(e){
        e.preventDefault()
        var description = $(this).siblings(".reason-description-text").html()
        $.fancybox({
            content: description,
            maxWidth: 820,
            padding: [30,30,100,74],
            beforeClose: function(){
                $("#reason-list").iosSlider('autoSlidePlay')
            }
        })
        $("#reason-list").iosSlider('autoSlidePause')
    })
})