function appendIndicator(carousel) {
 var myCarousel = $('carousel');
  myCarousel.append("<ol class='carousel-indicators'></ol>");
    var indicators = $(".carousel-indicators");
    myCarousel.find(".carousel-inner").children(".item").each(function(index) {
      (index === 0) ?
       indicators.append("<li data-target= '"+ carousel + "' data-slide-to='"+index+"' class='active'></li>") :
       indicators.append("<li data-target='" + carousel + "' data-slide-to='"+index+"'></li>");
    })


}

$('.carousel').carousel();

appendIndicator('#myCarousel');