
function meGustaPlato(platoSlug, megustaantes)
{
	$.get( "/resta/megustaplato/"+platoSlug, function( data ) {
		if(data == 'OK')
		{
			megustaantes++;
			$( "#meGustaContador" ).html( megustaantes );
		}
		else
		{
			alert("Ya has votado antes!");
		}
	});
}
