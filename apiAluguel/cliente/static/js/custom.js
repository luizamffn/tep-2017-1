//import axios from 'axios';

//axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
//axios.defaults.xsrfCookieName = "XCSRF-TOKEN";

$( window ).on( "load", function() {
  $('.tooltipped').tooltip({delay: 50});
  $(".dropdown-button").dropdown({
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false,
    hover: false,
    gutter: 0,
    belowOrigin: true,
    alignment: 'left',
    stopPropagation: false
  });
});