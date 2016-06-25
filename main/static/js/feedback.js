$(function(){
    var $form = $("#feedback_form")
    var $resultPlace = $form.parent()
    $form.ajaxForm({
        target: $resultPlace,
        beforeSubmit: function(){
            $("<div id=wait />").hide().appendTo($resultPlace).fadeIn("fast")
        },
        success: function(){
            setTimeout(function(){$.fancybox.close()}, 4000)
        }
    })
})