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
			vid.addEventListener('ended', function(ev) {
				vid.currentTime = 0.1;
				vid.play();
			});
			vid.addEventListener('loadeddata', function(ev) {
				console.log('loaded video');
				vid.play();
				fn();
				setTimeout(function () {
					$(vid).removeClass('hide');
					$(vid).addClass('fadeIn');
					$('.loader').addClass('hide');
					$('.intro').removeClass('hide');
					$('.intro div').typed({
						strings:["^500 Hey, ^500 I'm Dave the dev. ^500<br>That's me on the right. ^200<br>That's where I live. ^300<br>Nice to meet you. ^500<br>Welcome to my <a href='/'>site</a>. ^500"],
						showCursor: false,
						typeSpeed: 20
					});
					$('.print').addClass('hide');
				}, 1000);
			});
		}
	}, {
		name: 'fonts',
		load: function (fn) {
			var start = new Date().getTime();
			WebFontConfig = {
			  google: { families: ['Dancing+Script::latin'] },
			  fontactive: function(familyName, fvd) {
			  	console.log('loaded font');
				fn()
			  },
			};
			getGoogleFonts();
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

function getGoogleFonts() {
  var wf = document.createElement('script');
  wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
    '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
  wf.type = 'text/javascript';
  wf.async = 'true';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(wf, s);
};
