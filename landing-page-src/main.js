include "loadPrinter.js"

include "typer.js"

var resources = [
	{
		name: 'javascript',
		load: function(fn) {
			$script('/assets/js/landing-page-libs.min.js', 'libs');
			$script.ready(['libs'], fn);
		}
	}, {
		name: 'vid',
		load: function(fn) {
			var vid = document.querySelector('video');
			vid.addEventListener('progress', function(ev) {
				console.log('progress');
			});
			vid.addEventListener('loadeddata', function(ev) {
				console.log('loaded video');
				setTimeout(function () {
					// $(vid).removeClass('hide');
					// $('.loader').addClass('hide');
					$('.intro').removeClass('hide');
					$('.intro div').typed({
						strings:["Hey, ^500 I'm Dave the dev. ^500<br>This is where I live. ^500<br>This is my <a href='/'>site</a>. ^500"],
						showCursor: false,
						typeSpeed: 20
					});
					// $('.print').empty();
				}, 1000);
				fn();
			});
		}
	}
];

var printHello = function (printElement) {
	var div = document.createElement('div');
	printElement.appendChild(div);
	var typer = new Typer(div);
	typer.type('Hey give me a sec :-)');
}

var printElement = document.querySelector('main .print');

printHello(printElement);

for (var i = 0; i < resources.length; i ++) {
	var resource = resources[i];
	var loader = new LoadPrinter(resource, printElement);
}