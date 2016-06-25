$(function(){

var Apartments = {
    ANIMATION_DURATION: 800,
    Switch2Building: function(hash){
        var app = this,
            hashArray = hash.split('/'),
            BuildingCode = hashArray[0],
            $selectedBuildingItem = $('.building-section li[data-building='+BuildingCode+']'),
            $selectedBuildingMenu = $('.building-info-item[data-building='+BuildingCode+'] .building-menu ul'),
            $selectedBuildingMenuItem = $selectedBuildingMenu.children('li.selected'),
            $arrow = $('.building-section .arrow_place .arrow')
        $('.building-section li').removeClass('selected')
        $selectedBuildingItem.addClass('selected')
        $arrow.animate({top:$selectedBuildingItem.offset().top-$('.building-section').offset().top-2})
        $('.building-info-item').hide().filter('[data-building='+BuildingCode+']').show()
        if(hashArray.length<3){
            app.HideAptInfo()
            if($selectedBuildingMenuItem.size()==1){
                hash = $selectedBuildingMenuItem.find('a').attr('href').replace('#','')
            }
            window.location.hash = hash
        }
    },
    SwitchInfoType: function(infoType){
        var app=this,
            hash = window.location.hash.replace('#',''),
            hashArray = hash.split('/'),
            $menu = $('.building-info-item:visible'),
            $page = $menu.closest('.building-info-item')
        $menu.find('li').removeClass('selected').filter('.'+infoType).addClass('selected')
        $menu.find('.building-info-page').removeClass('selected').filter('.'+infoType).addClass('selected')
        if(infoType=='apartments'){
            var $aptPlace = $menu.find('.building-info-page.apartments .apt-list-content')
            if($.trim($aptPlace.text())==''){
                $aptPlace.addClass("load").load("/apartments/"+$menu.data("building")+"/", function(){
                    $aptPlace.removeClass("load")
                    app.FiltersInit($page)
                    if(hashArray[2]){
                        app.ShowApt('/apartments/'+hash)
//                        $.ajax({
//                            url: '/apartments/'+hash,
//                            success: function(data){
//                                $('#apt-info').css({left:383}).html(data)
//                            }
//                        })
                    }
                })
            }
        }else if(infoType=='photos'){
            setTimeout(app.SetupGallery, 10)
        }
        if(hashArray.length<2||infoType!='apartments'){
            app.HideAptInfo()
        }
        var top = $menu.find('li.selected').offset().top - $menu.find('.building-menu').offset().top + 51
        $menu.find('.focus').animate({top:top})
    },
    ShowApt: function(url){
        var app = this,
            $aptInfo = $('#apt-info')
        if(!$aptInfo.hasClass('active')){
            var $aptInfoBlock = $('<div class=apt-info-content>').appendTo($aptInfo),
                $aptDataBlock = $('<div class=apt-data>').appendTo($aptInfoBlock)
            $aptInfo.addClass('active').animate({left:383}, {duration: app.ANIMATION_DURATION})
            $aptDataBlock
                .addClass("load")
                .load(url, function(){
                    $aptDataBlock.removeClass("load")
                })
        }else{
            var $aptInfoBlock = $aptInfo.find('.apt-info-content'),
                $aptOldInfo = $aptInfo.find('.apt-data'),
                $aptNewInfo = $('<div class=apt-data>').appendTo($aptInfo.find('.apt-info-content'))
            $aptInfoBlock.height($aptInfoBlock.height())
            $aptOldInfo.addClass('old').fadeOut(app.ANIMATION_DURATION, function(){
                $(this).remove()
            })
            $aptNewInfo
                .css({opacity:0})
                .animate({opacity:1},{duration:app.ANIMATION_DURATION})
                .load(url, function(){
                    $aptInfoBlock.removeClass("load").css({height:'auto'})
                })
        }
    },
    HideAptInfo: function(){
        var app = this,
            hashArray = window.location.hash.replace('#','').split('/')
//        window.location.hash = hashArray.slice(0,2).join('/')
        $('.apt-info-content').addClass('hide-out')
        $('#apt-info').removeClass('active')
        setTimeout(function(){
            $('#apt-info').css({left:'100%'}).empty()
        },app.ANIMATION_DURATION)
    },
    SetupGallery: function(){
        var $activeBuilding = $('.building-info-item:visible'),
            $largeSlider = $activeBuilding.find('.large-photos .iosSlider'),
            $thumbSlider = $activeBuilding.find('.small-photos .iosSlider'),
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
    },
    SetMap: function(){
        ymaps.ready(function(){
            var map = new ymaps.Map ("map", {
                center: [44.554488,38.062433],
                zoom: 17
            }),
                buildings = {}

            map
                .setType('yandex#hybrid')
                .controls
                    .add('zoomControl',{left:20,top:5})
                    .add('miniMap',{left:20,bottom:5})
                    .add('typeSelector')

            buildings['CM'] = new ymaps.Polygon([[[44.555343,38.061795],[44.555225,38.064219],[44.554941,38.064134],[44.555079,38.061736]]],{hintContent: "Клод Моне"},{fillOpacity:0,strokeWidth:0})
            buildings['BM'] = new ymaps.Polygon([[[44.553468,38.063216],[44.553399,38.063533],[44.553291,38.063844],[44.553107,38.06371],[44.553161,38.063377],[44.553276,38.063077]]],{hintContent: "Берта Моризо"},{fillOpacity:0,strokeWidth:0})
            buildings['OR'] = new ymaps.Polygon([[[44.553886,38.062471],[44.553771,38.062803],[44.55346,38.063222],[44.553295,38.063098],[44.553403,38.062755],[44.55369,38.062379]]],{hintContent: "Пьер Огюст Ренуар"},{fillOpacity:0,strokeWidth:0})
            buildings['FB'] = new ymaps.Polygon([[[44.55425,38.062846],[44.554124,38.063184],[44.553894,38.063125],[44.553752,38.063002],[44.553859,38.062674],[44.554089,38.062728]]],{hintContent: "Фредерик Базиль"},{fillOpacity:0,strokeWidth:0})
            buildings['AS'] = new ymaps.Polygon([[[44.554327,38.063468],[44.554231,38.063779],[44.554001,38.06372],[44.553851,38.063592],[44.553955,38.063265],[44.55417,38.063334]]],{hintContent: "Альфред Сислей"},{fillOpacity:0,strokeWidth:0})
            buildings['CP'] = new ymaps.Polygon([[[44.554613,38.061084],[44.554636,38.061333],[44.554559,38.061725],[44.554388,38.061733],[44.554373,38.061508],[44.554409,38.061111]]],{hintContent: "Камиль Писсаро"},{fillOpacity:0,strokeWidth:0})
            buildings['ED'] = new ymaps.Polygon([[[44.554515,38.060435],[44.554594,38.060746],[44.554599,38.061049],[44.554408,38.061092],[44.554316,38.060786],[44.554293,38.060454]]],{hintContent: "Эдгар Дега"},{fillOpacity:0,strokeWidth:0})
            map.geoObjects
                .add(buildings['CM'])
                .add(buildings['BM'])
                .add(buildings['OR'])
                .add(buildings['FB'])
                .add(buildings['AS'])
                .add(buildings['CP'])
                .add(buildings['ED'])
            for(i in buildings){
                function addClickHandler(i){
                    buildings[i].events.add('click', function(){$('.building-list>[data-building='+i+']>a').click()})
                }
                addClickHandler(i)
            }
        })
    },
    NumberFormat: function(number, decimals, dec_point, thousands_sep){
        number = (number + '').replace(/[^0-9+\-Ee.]/g, '');
        var n = !isFinite(+number) ? 0 : +number,
            prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
            sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
            dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
            s = '',
            toFixedFix = function (n, prec) {
                var k = Math.pow(10, prec)
                return '' + Math.round(n * k) / k
            }
        s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.')
        if (s[0].length > 3) {
            s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep)
        }
        if ((s[1] || '').length < prec) {
            s[1] = s[1] || ''
            s[1] += new Array(prec - s[1].length + 1).join('0')
        }
        return s.join(dec)
    },
    Filter: function(){
        var resultCount = 0
        $('#apt-list tbody tr').each(function(){
            var $row = $(this),
                $filter = $row.closest('.building-info-page').find('.filter-head'),
                needShow = true,
                filterCode = $.trim($filter.find('.filter-code').val()),
                aptCode = $.trim($row.find('.apt-code').text()),
                filterPriceMin = parseInt($.trim($filter.find('.filter-part.price').data("filter-min-price"))),
                filterPriceMax = parseInt($.trim($filter.find('.filter-part.price').data("filter-max-price"))),
                aptPrice = parseInt($.trim($row.find('.apt-price').data("price"))),
                $filterStatus = $filter.find('.filter-part.status'),
                aptStatus = parseInt($.trim($row.find('.apt-status').data("status"))),
                filterSquareMin = parseInt($.trim($filter.find('.filter-part.square').data("filter-min-square"))),
                filterSquareMax = parseInt($.trim($filter.find('.filter-part.square').data("filter-max-square"))),
                aptSquare = parseInt($.trim($row.find('.apt-square').data("square"))),
                $filterLayout = $filter.find('.filter-part.layout'),
                aptLayout = parseInt($.trim($row.find('.apt-layout').data("layout"))),
                $filterSea = $filter.find('.filter-sea'),
                aptSea = $.trim($row.find('.apt-layout').data("sea")),
                $filterTerrace = $filter.find('.filter-terrace'),
                aptTerrace = $.trim($row.find('.apt-layout').data("terrace")),
                $filterLawn = $filter.find('.filter-lawn'),
                aptLawn = $.trim($row.find('.apt-layout').data("lawn")),
                filterStatus = [],
                filterLayout = []

            if(aptCode.indexOf(filterCode)<=-1) needShow = false
            else if (aptPrice<filterPriceMin||aptPrice>filterPriceMax) needShow = false
            else if (aptSquare<filterSquareMin||aptSquare>filterSquareMax) needShow = false
            else if ($filterSea.is(':checked')&&aptSea=='False') needShow = false
            else if ($filterTerrace.is(':checked')&&aptTerrace=='False') needShow = false
            else if ($filterLawn.is(':checked')&&aptLawn=='False') needShow = false
            else {
                filterStatus = $filterStatus.data('statuses')

                if(typeof filterStatus != 'undefined'){
                    if(filterStatus.length>0){
                        needShow = false
                        for(i in filterStatus){
                            if(aptStatus==filterStatus[i]){
                                needShow = true
                            }
                        }
                    }
                }
                if(needShow){
                    filterLayout = $filterLayout.data('layouts')
                    if(typeof filterLayout != 'undefined'){
                        if(filterLayout.length>0){
                            needShow = false
                            for(i in filterLayout){
                                if(aptLayout==filterLayout[i]){
                                    needShow = true
                                    break
                                }
                            }
                        }
                    }
                }
            }
            if(needShow) {
                $row.show()
                resultCount++
            }
            else $row.hide()
        })
        if(resultCount>0){
            $('.building-info-item:visible .no-result').hide()
        } else {
            $('.building-info-item:visible .no-result').show()
        }
    },
    FiltersInit: function($page){
        var app = this,
            $pLink = $page.find('[rel=popover]'),
            pt = $.fn.popover.Constructor.prototype.show
        $.fn.popover.Constructor.prototype.show = function () {
            pt.call(this)
            if (this.options.callback) {
                this.options.callback()
            }
        }
        $pLink.each(function(){
            var $this = $(this),
                $fPart = $this.closest('.filter-part'),
                $table = $this.closest('.building-info-page').find('table.apt-list')
            $this.popover({
                html : true,
                placement: 'bottom',
                content: function() {
                    return $fPart.find('.popover-content').html()
                },
                callback: function(){
                    if($fPart.hasClass('status')){
                        var statuses = $fPart.data('statuses')

                        $fPart.find(':checkbox').prop('checked',false)
                        if(statuses){
                            for(i in statuses){
                                $fPart.find(':checkbox[data-status='+statuses[i]+']').prop('checked',true)
                            }
                        }
                    }else if($fPart.hasClass('layout')){
                        var layouts = $fPart.data('layouts')
                        if(layouts){
                            for(i in layouts){
                                $fPart.find('.popover :checkbox[data-layout='+layouts[i]+']').prop('checked',true)
                            }
                        }
                        var pluses = $fPart.data('pluses')
                        if(pluses){
                            for(i in pluses){
                                $fPart.find('.popover :checkbox[data-plus='+pluses[i]+']').prop('checked',true)
                            }
                        }
                    }
                }
            })
            if($fPart.hasClass("price")){
                var $minValue = $fPart.find('.min-value'),
                    $maxValue = $fPart.find('.max-value'),
                    initMinPrice = $table.data('minprice'),
                    initMaxPrice = $table.data('maxprice')
                $fPart
                    .data("min-price",initMinPrice)
                    .data("max-price",initMaxPrice)
                    .data("filter-min-price",initMinPrice)
                    .data("filter-max-price",initMaxPrice)
                $minValue.text(app.NumberFormat(initMinPrice,0,'',' '))
                $maxValue.text(app.NumberFormat(initMaxPrice,0,'',' '))
                $pLink.click(function(){
                    $fPart.find('.popover .slider').slider({
                        range: true,
                        min: $fPart.data('min-price'),
                        max: $fPart.data('max-price'),
                        values: [$fPart.data('filter-min-price'),$fPart.data('filter-max-price')],
                        slide: function( event, ui ) {
                            $fPart.find('.min-value').text(app.NumberFormat(ui.values[0],0,'',' '))
                            $fPart.find('.max-value').text(app.NumberFormat(ui.values[1],0,'',' '))
                            $fPart
                                .data("filter-min-price",ui.values[0])
                                .data("filter-max-price",ui.values[1])
                            var $value = $fPart.find('.value'), value = $value.data('default')
                            if(ui.values[0]>initMinPrice||ui.values[1]<initMaxPrice){
                                value = 'от '+app.NumberFormat(ui.values[0]/1000000,1,',')+' до '+app.NumberFormat(ui.values[1]/1000000,1,',')+' млн. ⃆'
                            }
                            $value.text(value)
                            app.Filter()
                        }
                    })
                })
            } else if($fPart.hasClass("square")){
                var $minValue = $fPart.find('.min-value'),
                    $maxValue = $fPart.find('.max-value'),
                    initMinSquare = parseFloat($table.data('minsquare')),
                    initMaxSquare = parseFloat($table.data('maxsquare'))
                $fPart
                    .data("min-square",initMinSquare)
                    .data("max-square",initMaxSquare)
                    .data("filter-min-square",initMinSquare)
                    .data("filter-max-square",initMaxSquare)
                $minValue.text(app.NumberFormat($fPart.data('min-square'),1,',',' '))
                $maxValue.text(app.NumberFormat($fPart.data('max-square'),1,',',' '))
                $pLink.click(function(){
                    $fPart.find('.popover .slider').slider({
                        range: true,
                        min: $fPart.data('min-square'),
                        max: $fPart.data('max-square'),
                        step: 0.1,
                        values: [$fPart.data('filter-min-square'),$fPart.data('filter-max-square')],
                        slide: function( event, ui ) {
                            $fPart.find('.min-value').text(app.NumberFormat(ui.values[0],1,',',' '))
                            $fPart.find('.max-value').text(app.NumberFormat(ui.values[1],1,',',' '))
                            $fPart
                                .data("filter-min-square",ui.values[0])
                                .data("filter-max-square",ui.values[1])
                            var $value = $fPart.find('.value'), value = $value.data('default')
                            if(ui.values[0]>initMinSquare||ui.values[1]<initMaxSquare){
                                value = 'от '+app.NumberFormat(ui.values[0],1,',')+' до '+app.NumberFormat(ui.values[1],1,',')+' м<sup>2</sup>'
                            }
                            $value.html(value)
                            app.Filter()
                        }
                    })
                })
            }
        })
        $('body').on('click', function (e) {
            $pLink.each(function(){if(!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) { $(this).popover('hide')}})
        })
        $('.filter-part').on('click', 'button.ok', function(){
            $(this).closest('.popover').siblings('[rel=popover]').popover('hide')
        })
        $('.filter-part.status').on('click', '.popover :checkbox', function(){
            var $checkbox = $(this),
                $fPart = $checkbox.closest('.filter-part'),
                statuses = [],
                verbose_statuses = [],
                $value = $fPart.find('.value'),
                value = $value.data('default')
            $fPart.find('.popover :checkbox:checked').each(function(){
                var cStatus = parseInt($(this).data('status'))
                statuses.push(cStatus)
                switch(cStatus){
                    case 0: verbose_statuses.push('доступные'); break
                    case 1: verbose_statuses.push('забронированные'); break
                    case 2: verbose_statuses.push('проданные'); break
                }
            })
            if(verbose_statuses.length>0&&verbose_statuses.length<3) value = verbose_statuses.join(' и ')
            $value.text(value)
            $fPart.data({statuses: statuses})
            app.Filter()
        })
        $('.filter-part.layout').on('click', '.popover :checkbox', function(){
            var $checkbox = $(this),
                $fPart = $checkbox.closest('.filter-part'),
                layouts = [],
                pluses = [],
                verbose_layouts = [],
                verbose_pluses = [],
                $value = $fPart.find('.value'),
                value = $value.data('default'),
                value_filtered = []
            $fPart.find('.popover [data-layout]:checkbox:checked').each(function(){
                var cLayout = parseInt($(this).data('layout'))
                layouts.push(cLayout)
                switch(cLayout){
                    case 1: verbose_layouts.push('сутдии'); break
                    case 2: verbose_layouts.push('2к'); break
                    case 3: verbose_layouts.push('3к'); break
                    case 4: verbose_layouts.push('свободные'); break
                    case 5: verbose_layouts.push('2-ур'); break
                }
            })
            $fPart.find('.popover [data-plus]:checkbox:checked').each(function(){
                var cPlus = $(this).data('plus')
                pluses.push(cPlus)
                switch(cPlus){
                    case 'sea': verbose_pluses.push('видом на море'); break
                    case 'terrace': verbose_pluses.push('террасой'); break
                    case 'lawn': verbose_pluses.push('лужайкой'); break
                }
            })
            if(verbose_layouts.length>0&&verbose_layouts.length<5) value_filtered.push(verbose_layouts.join(', '))
            if(verbose_pluses.length>0&&verbose_pluses.length<4) value_filtered.push('с '+verbose_pluses.join(', '))
            if(value_filtered.length>0) value = value_filtered.join('<br>')
            $value.html(value)
            $fPart.data({layouts: layouts})
            $fPart.data({pluses: pluses})
            app.Filter()
        })
    },
    SmartHash: function(){
        var app = this,
            hash = window.location.hash.replace("#",""),
            hashArray = hash.split('/')

        if(hashArray.length>0){
            app.Switch2Building(hash)
            if(hashArray.length>1){
                app.SwitchInfoType(hashArray[1])
            }
        }
    },
    Init: function(){
        var app = this
        app.SetMap()
        $('.building-section a').click(function(e){
            e.preventDefault()
            var $this = $(this),
                hash = $this.attr("href").replace("#", "")
            app.Switch2Building(hash)
        })
        $('.building-menu a').click(function(e){
            e.preventDefault()
            var $this = $(this)
            window.location.hash = $this.attr("href")
            app.SwitchInfoType($this.data('type'))
        })
        $('body').on('click', '.apt-detail-link', function(e){
            e.preventDefault()
            var $this = $(this)
            window.location.hash = $this.attr("href")
            app.ShowApt($this.attr("href").replace("#", ""))
        })
        $('.apt-app').on('click', '.close', function(e){
            e.preventDefault()
            app.HideAptInfo()
        })
        $('.filter-code').keyup(app.Filter)
        app.SmartHash()
    }

}

Apartments.Init()

})