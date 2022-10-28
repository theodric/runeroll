 /*
 *
 * Theme functions
 * Initialize all scripts and adds custom js
 *
 * Version 1.0
 */
( function( $ ) {
    "use strict";

    $(document).ready( function() {
    ///////////////////////////////


        /////////////////////////////////
        // Sticky Sidebar
        /////////////////////////////////
        jQuery('.sidebar').stick_in_parent({parent: '.wrap-fullwidth, .wrap-container', spacer: '.sidebar-wrapper'});

 
        /////////////////////////////////
        // Grid + Infinite Scroll
        /////////////////////////////////
        var $container = jQuery( '#infinite-articles' );
        $container.imagesLoaded( function(){
            $container.masonry( {
                itemSelector        : '.ms-item',
                transitionDuration  : '0.5s',
                isOriginLeft: true 
            } );
        } );

        // Infinite scroll
        var $container = jQuery( '#infinite-articles' );
        $container.infinitescroll( {
                loading : {
                    msg         : null,
                    finishedMsg : '',
                    msgText     : '<span><i class="fa fa-spinner fa-spin"></i> Loading ...</span>',
                },
                navSelector     : '#nav-below',
                nextSelector    : '#nav-below a',
                itemSelector    : '.ms-item',
                },
                // trigger Masonry as a callback
                function( newElements ) {
                    // hide new items while they are loading
                    var $newElems = jQuery( newElements ).css( { opacity: 0 } );
                    // ensure that images load before adding to masonry layout
                    $newElems.imagesLoaded( function(){
                        // Slider
                        // show elems now they're ready
                        $(".sidebar").stick_in_parent({recalc_every: 1}); // infinite scroll + sticky
                        $newElems.animate( { opacity: 1 } );
                        $container.masonry( 'appended', $newElems, true );
                } );
        } );


        /////////////////////////////////
        // Accordion 
        /////////////////////////////////       
        jQuery(".accordionButton").click(function(){jQuery(".accordionButton").removeClass("on");jQuery(".accordionContent").slideUp("normal");if(jQuery(this).next().is(":hidden")==true){jQuery(this).addClass("on");jQuery(this).next().slideDown("normal")}});jQuery(".accordionButton").mouseover(function(){jQuery(this).addClass("over")}).mouseout(function(){jQuery(this).removeClass("over")});jQuery(".accordionContent").hide(); 


        /////////////////////////////////
        // Go to TOP
        /////////////////////////////////
        // hide #back-top first
        jQuery("#back-top").hide();
        
        // fade in #back-top
        jQuery(function () {
            jQuery(window).scroll(function () {
                if (jQuery(this).scrollTop() > 100) {
                    jQuery('#back-top').fadeIn();
                } else {
                    jQuery('#back-top').fadeOut();
                }
            });

            // scroll body to 0px on click
            jQuery('#back-top a').click(function () {
                jQuery('body,html').animate({
                    scrollTop: 0
                }, 800);
                return false;
            });
        });


        /////////////////////////////////
        // Menu & link arrows
        /////////////////////////////////
        // alert(list_mag_wp_js_custom.template_url+'/images/menu/arrow-down.png');
        var jquerycssmenu={fadesettings:{overduration:0,outduration:100},buildmenu:function(b,a){jQuery(document).ready(function(e){var c=e("#"+b+">ul");var d=c.find("ul").parent();d.each(function(g){var h=e(this);var f=e(this).find("ul:eq(0)");this._dimensions={w:this.offsetWidth,h:this.offsetHeight,subulw:f.outerWidth(),subulh:f.outerHeight()};this.istopheader=h.parents("ul").length==1?true:false;f.css({top:this.istopheader?this._dimensions.h+"px":0});h.children("a:eq(0)").css(this.istopheader?{paddingRight:a.down[2]}:{}).append('<img src="'+(this.istopheader?a.down[1]:a.right[1])+'" class="'+(this.istopheader?a.down[0]:a.right[0])+'" style="border:0;" />');h.hover(function(j){var i=e(this).children("ul:eq(0)");this._offsets={left:e(this).offset().left,top:e(this).offset().top};var k=this.istopheader?0:this._dimensions.w;k=(this._offsets.left+k+this._dimensions.subulw>e(window).width())?(this.istopheader?-this._dimensions.subulw+this._dimensions.w:-this._dimensions.w):k;i.css({left:k+"px"}).fadeIn(jquerycssmenu.fadesettings.overduration)},function(i){e(this).children("ul:eq(0)").fadeOut(jquerycssmenu.fadesettings.outduration)})});c.find("ul").css({display:"none",visibility:"visible"})})}};
        var arrowimages={down:['downarrowclass', (list_mag_wp_js_custom.template_url+'/images/menu/arrow-down.png')], right:['rightarrowclass', (list_mag_wp_js_custom.template_url+'/images/menu/arrow-right.png')]}; jquerycssmenu.buildmenu("myjquerymenu", arrowimages); jquerycssmenu.buildmenu("myjquerymenu-cat", arrowimages);
 

    //////////////////////////////
    } ); // End doc ready  ///////
    
} )( jQuery );