$(document).ready(function () {
	$('.hamburger').click(function () {
		$('body').toggleClass('show-sidebar')
	})

	var canvas, ctx;
	$('#statistics-canvas').each(function() {
		canvas = $(this)[0];
		console.log(canvas)
		ctx = canvas.getContext('2d');

		var data = $(this).data('canvas-data');

		var barcolor='#b0d6d9';
		drawHistogram(data, barcolor);
	})

	function drawHistogram(data, barcolor){
		ctx.save();

		ctx.font = 'italic 20pt Calibri';
		ctx.fillStyle=barcolor;
		barwidth=120;
		barspace=20;
		barunit=10;

		var posX = 0;
		var posY = 0;
		for (var i=0; i<data.length; i++){
			console.log(data[i])
			barheight=data[i].qty * barunit;
			posX = i*barspace + i*barwidth;
			posY = 300 - barheight;
			ctx.fillRect(posX, posY, barwidth, barheight);
			ctx.save();
			ctx.fillStyle='black';
			ctx.fillText(data[i].name + " - " + data[i].qty, posX, posY - 20);
			ctx.restore();
		}

		ctx.restore();
	}
});