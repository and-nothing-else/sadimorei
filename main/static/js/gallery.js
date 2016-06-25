$(function(){
    var $gallery = $('#gallery'),
        $largeSlider = $gallery.find('.large-photos .iosSlider'),
        $thumbSlider = $gallery.find('.small-photos .iosSlider'),
        $buttons = $thumbSlider.find('.button')
    $largeSlider.iosSlider({
        snapToChildren: true,
        desktopClickDrag: true,
        infiniteSlider: false,
        onSliderLoaded: SliderCallback,
        onSlideChange: SliderCallback
    })
    $thumbSlider.iosSlider({
        snapToChildren: true,
        desktopClickDrag: true,
        infiniteSlider: false
    })
    $buttons.each(function(i) {
        $(this).bind('click', function() {
            $largeSlider.iosSlider('goToSlide', i+1)
        })
    })
    function SliderCallback(args) {
        var currentSlide = args.currentSlideNumber
        $thumbSlider.iosSlider('goToSlide', currentSlide)
        $buttons.removeClass('selected').eq(args.currentSlideNumber-1).addClass('selected')
        $(args.sliderObject).find('.description').attr('style', '');
        $(args.currentSlideObject).find('.description')
            .animate({opacity: 1, bottom: 13}, 400, 'linear')
    }
})