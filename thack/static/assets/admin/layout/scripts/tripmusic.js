/**
Demo script to handle the theme demo
**/
var TripMusic = function () {

    // Handle Theme Settings
    var handleInit = function () {
    	$.getJSON( "api/show", function( data ) {
			var items = [];
			$.each(data, function( key, eventi ) {
				items.push( '<a data-toggle="modal" href="eventDetail?event_id=' + eventi.id + '" data-target="#myModal"> ' +
							'<div class="tile double bg-blue-madison"> ' +
							'	<div class="tile-body">  ' +
							'		<img src="' + eventi.image + ' " alt="" width="60" height="60">   ' +
							'		<h4>' + eventi.name + ' </h4>  ' +
							'	</div>  ' +
							'	<div class="tile-object">  ' +
							'		<div class="name">  ' +
							'			$' + eventi.price  +
							'		</div>  ' +
							'		<div class="number">  ' +
										$.datepicker.formatDate('dd/mm/yy', new Date(eventi.datetime)) +
							'		</div>  ' +
							'	</div>  ' +
							'</div></a>');
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