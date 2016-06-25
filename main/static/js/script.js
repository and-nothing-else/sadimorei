$(function(){
    function feedbackPopup(e){
        e.preventDefault()
        var fb_link = $(this).attr("href")
        $.fancybox({
            href: fb_link,
            type: 'ajax'
        })
    }
    $("#feedback_link, #feedback_commercial").click(feedbackPopup)
    $('.apt-app').on('click', '#feedback_er404', feedbackPopup)
    $("#menu-expand").on("click touchstart",function(){$(".submenu").slideToggle(600).closest(".head-content").toggleClass("open")})
    $(".middle_content").on("click touchstart",function(){$(".submenu").slideUp(600).closest(".head-content").removeClass("open")})
})