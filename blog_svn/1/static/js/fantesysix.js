$(function() {
	$( "#origin-cards" ).sortable();
	$( "#origin-cards" ).disableSelection();

	$('#confirm').on('click', function(){
		selectedCards = $('#origin-cards .card');
		// console.log(selectedCards);
		cards = []
		for (var i = 0; i < selectedCards.length; i++) {
			cards.push($(selectedCards[i]).attr('name'));
		};
		// console.log(cards);
		$.ajax({
			url: '/fantesysixjudge',
			type: 'post',
			dataType: 'html',
			data: {selectedCards: cards},
		})
		.done(function(html) {
			$('.container').html(html);
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
		
	});

	$('#playAgain').on('click', function(){
		var url = $('#playAgain').attr('url');
		$.ajax({
			url: url,
			type: 'post',
			dataType: 'html'
		})
		.done(function(html) {
			$('.container').html(html);
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
		
	});
});
