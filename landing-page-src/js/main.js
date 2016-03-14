var resources = [{
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
				$(vid).removeClass('hide');
				$(vid).addClass('fadeIn');
				$('.intro').removeClass('hide');
				var message = "^500 I'm Dave the dev. ^500<br>That's me on the right. ^200" +
					"<br/>Welcome to my <a href='/'>site</a> ^500";
				$('.intro-text-content span').typed({
					strings:["^500 Hey", message],
					showCursor: true,
					typeSpeed: 20
				});
				$('.print').addClass('hide');
			});
		}
	}, {
		name: 'fonts',
		load: function (fn) {
			var start = new Date().getTime();
			WebFontConfig = {
			  google: { families: ['Ubuntu:300:latin'] },
			  fontactive: function(familyName, fvd) {
			  	console.log('loaded font');
				fn()
			  },
			};
			getGoogleFonts();
		}
	}
];

var isMobile = !function(a){var b=/iPhone/i,c=/iPod/i,d=/iPad/i,e=/(?=.*\bAndroid\b)(?=.*\bMobile\b)/i,f=/Android/i,g=/IEMobile/i,h=/(?=.*\bWindows\b)(?=.*\bARM\b)/i,i=/BlackBerry/i,j=/BB10/i,k=/Opera Mini/i,l=/(?=.*\bFirefox\b)(?=.*\bMobile\b)/i,m=new RegExp("(?:Nexus 7|BNTV250|Kindle Fire|Silk|GT-P1000)","i"),n=function(a,b){return a.test(b)},o=function(a){var o=a||navigator.userAgent;return this.apple={phone:n(b,o),ipod:n(c,o),tablet:n(d,o),device:n(b,o)||n(c,o)||n(d,o)},this.android={phone:n(e,o),tablet:!n(e,o)&&n(f,o),device:n(e,o)||n(f,o)},this.windows={phone:n(g,o),tablet:n(h,o),device:n(g,o)||n(h,o)},this.other={blackberry:n(i,o),blackberry10:n(j,o),opera:n(k,o),firefox:n(l,o),device:n(i,o)||n(j,o)||n(k,o)||n(l,o)},this.seven_inch=n(m,o),this.any=this.apple.device||this.android.device||this.windows.device||this.other.device||this.seven_inch,this.phone=this.apple.phone||this.android.phone||this.windows.phone,this.tablet=this.apple.tablet||this.android.tablet||this.windows.tablet,"undefined"==typeof window?this:void 0},p=function(){var a=new o;return a.Class=o,a};"undefined"!=typeof module&&module.exports&&"undefined"==typeof window?module.exports=o:"undefined"!=typeof module&&module.exports&&"undefined"!=typeof window?module.exports=p():"function"==typeof define&&define.amd?define("isMobile",[],a.isMobile=p()):a.isMobile=p()}(this);

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
