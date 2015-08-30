/**
Demo script to handle the theme demo
**/
var TripMusic = function () {

    // Handle Theme Settings
    var handleInit = function () {
    	$.getJSON( "http://www.mocky.io/v2/55e1fd0ecd3fddc306fdb10f", function( data ) {
			var items = [];
			
			$.each(data.events, function( key, eventi ) {
				items.push( '<div class="tile double bg-blue-madison"> ' +
							'	<div class="tile-body">  ' +
							'		<img src="' + eventi.image + ' " alt="" width="60" height="60">   ' +
							'		<h4>' + eventi.name + ' </h4>  ' +
							'		<p> ' +
							 			eventi.description +
							'		</p> ' +
							'	</div>  ' +
							'	<div class="tile-object">  ' +
							'		<div class="name">  ' +
										eventi.price.toFixed(2)  +
							'		</div>  ' +
							'		<div class="number">  ' +
										$.datepicker.formatDate('dd/mm/yy', new Date(eventi.date)) +
							'		</div>  ' +
							'	</div>  ' +
							'</div>');
			});

			$( "#tilesBox" ).append( items.join( "" ));
		});
    }

    return {
       //main function to initiate the theme
        init: function() {
        	handleInit();
        }
    };

}();