$(function(){
    var $contactPage = $("#contact_page")
    var $contactList = $contactPage.find(".contact-list")
    var $contactLinks = $contactList.find("a.office")
    var $mapList = $contactPage.find(".map-holder")
    var $maps = $mapList.find(".map")
    var $pointer = $contactList.find(".pointer")

    function selectOffice(code) {
        var $contactLinkSelected = $contactLinks.filter("[data-office="+code+"]")
        if($contactLinkSelected.size()!=1){
            $contactLinkSelected = $contactLinks.first()
            code = $contactLinkSelected.data("office")
        }
        $contactLinks.removeClass("active").filter("[data-office="+code+"]").addClass("active")
        $maps.removeClass("active").filter("[data-office="+code+"]").addClass("active")
        var pointerTop = $contactLinkSelected.offset().top-$contactList.offset().top+5
        if($pointer.hasClass("indefinite")){
            $pointer.css({top: pointerTop}).fadeIn("slow")
            $pointer.removeClass("indefinite")
        }else{
            $pointer.animate({top: pointerTop})
        }
        window.location.hash = code
    }


    $("a.office").click(function(e){
        e.preventDefault()
        var code = $(this).data("office")
        selectOffice(code)
    })

    var officeSelected = window.location.hash.substr(1)
    selectOffice(officeSelected)
})