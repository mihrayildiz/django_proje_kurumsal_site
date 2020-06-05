// <![CDATA[
$(function() {

  // Slider
  $('#coin-slider').coinslider({width:960,height:335,opacity:1});

  // Radius Box
  $('.slider, .menu_nav, .content .mainbar img.fl, p.infopost, .post_content a.rm, .content p.pages span, .content p.pages a').css({"border-radius":"10px", "-moz-border-radius":"10px", "-webkit-border-radius":"10px"});
  $('.article a.com').css({"border-top-right-radius":"10px", "border-bottom-right-radius":"10px", "-moz-border-radius-topright":"10px", "-moz-border-radius-bottomright":"10px", "-webkit-border-top-right-radius":"10px", "-webkit-border-bottom-right-radius":"10px"});
  //$('.content p.pages span, .content p.pages a').css({"border-radius":"16px", "-moz-border-radius":"16px", "-webkit-border-radius":"16px"});
  //$('.menu_nav').css({"border-bottom-left-radius":"16px", "border-bottom-right-radius":"16px", "-moz-border-radius-bottomleft":"16px", "-moz-border-radius-bottomright":"16px", "-webkit-border-bottom-left-radius":"16px", "-webkit-border-bottom-right-radius":"16px"});

});	
$('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
  if (!$(this).next().hasClass('show')) {
    $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
  }
  var $subMenu = $(this).next(".dropdown-menu");
  $subMenu.toggleClass('show');


  $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
    $('.dropdown-submenu .show').removeClass("show");
  });


  return false;
});
// Cufon
Cufon.replace('h1, h2, h3, h4, h5, h6, .article a.com', { hover: true });
//Cufon.replace('h1', { color: '-linear-gradient(#fff, #ffaf02)'});
//Cufon.replace('h1 small', { color: '#8a98a5'});

// ]]>