$(document).ready(function() {

	/*Search suggestions*/
	$('#intro ul').hide();
	$('#intro input')
	.blur(function(){
		$(this).next().fadeOut("1");
	})
	.focus(function(){
		$(this).next().fadeIn("1");
	});

	var getUser=function() { 
					var name = $(this).val();
			        $.get('/dopomoga/get_UserInneed/', {name: name}, function(data){ $('#ui_name+datalist').html(data); } );
			    };
	$('#ui_name').one('click', getUser).keyup(getUser)

	var getRes=function() { 
					var name = $(this).val();
			        $.get('/dopomoga/get_Resource/', {name: name}, function(data){ $('#resource_name+ul').html(data); } );
			    };
	$('#resource_name').one('click', getRes).keyup(getRes)
	$('#resource_name+ul').click(function() { $('#resource_name').focus(); } )

	var getCause=function() { 
					var name = $(this).val();
			        $.get('/dopomoga/get_Cause/', {name: name}, function(data){ $('#cause_name+ul').html(data); } ); 
			    };
	$('#cause_name').one('click', getCause).keyup(getCause)
	$('#cause_name+ul').click(function() { $('#cause_name').focus(); } )
});

/*
$('input:checked+label').parent().css("background-color","green")
*/