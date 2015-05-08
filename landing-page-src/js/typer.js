function Typer(element, config) {
	config = config || {};
	this.element = element;
	this.charPause = config.charPause || 1;
	this.callback = config.callback || function () {};
}

Typer.prototype = {
	type: function (string, strPos) {
		var self = this;
		strPos = strPos || 0;
		self.isTyping = true;

		if (self._stop) {
			return;
		}

		if (self._complete) {
			self.element.innerText = string;
			return;
		}

		if (strPos === string.length) {
			self.isTyping = false;
			return self.callback();
		}

		var charPause = self.charPause * 30;
		var humanize = Math.round(Math.random() * (charPause * 3 - charPause));

		setTimeout(function () {
			self.element.innerText = string.substr(0, strPos + 1);
			strPos ++;
			self.type(string, strPos)
		}, humanize);
	},

	stop: function () {
		this._stop = true;
	},

	complete: function () {
		this._complete = true;
	}
};
