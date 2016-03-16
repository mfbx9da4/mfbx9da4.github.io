$(document).ready(function() {
	console.log($('h1.title'));
	$('h1.title').hover(function() {
		$('.profile-img').addClass('hover');
	});
	$('h1.title').mouseleave(function() {
		console.log('leave hover');
		$('.profile-img').removeClass('hover');
	});

	$('.profile-img').hover(function() {
		$('.hover-message').show();
		$('.hover-message').addClass('bounceInRight');
	});

	$('.profile-img').mouseleave(function() {
		$('.hover-message').hide();
		$('.hover-message').removeClass('bounceInRight');
	});

});
