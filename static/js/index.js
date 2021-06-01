$('#zoomBtn').click(function() {
  $('.zoom-btn-sm').toggleClass('scale-out');
  if (!$('.zoom-card').hasClass('scale-out')) {
    $('.zoom-card').toggleClass('scale-out');
  }
});

$('#machine_search').on('keyup', function() {
	console.log($(this).val());
	var value = $(this).val();

	$('.machine_list div').filter(function(){
		$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
	});
});

$('#machine_status_search').on('change', function() {
	var value = $(this).val();

	if (value === 'En renta' || value === 'Disponible') {

		console.log(value);
		// $('.machine_list div').filter(function() {
		// 	$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
		// });
		if ( value === 'En renta' ) {
			$('.not-available').show(500);
			$('.available').hide(500);
		} else if ( value === 'Disponible' ) {
			$('.not-available').hide(500);
			$('.available').show(500);
		}
	} else {
		$('.not-available').show(500);
		$('.available').show(500);
	}
});

// $('.zoom-btn-sm').click(function() {
//   var btn = $(this);
//   var card = $('.zoom-card');

//   if ($('.zoom-card').hasClass('scale-out')) {
//     $('.zoom-card').toggleClass('scale-out');
//   }
//   if (btn.hasClass('zoom-btn-person')) {
//     card.css('background-color', '#d32f2f');
//   } else if (btn.hasClass('zoom-btn-doc')) {
//     card.css('background-color', '#fbc02d');
//   } else if (btn.hasClass('zoom-btn-tangram')) {
//     card.css('background-color', '#388e3c');
//   } else if (btn.hasClass('zoom-btn-report')) {
//     card.css('background-color', '#1976d2');
//   } else {
//     card.css('background-color', '#7b1fa2');
//   }
// });
