

$(document).on('click', '#next-panel', function(e) {
	console.log("clicked")
	var panelNumberCurrent = $(this).val().split("-")[0];
	var panelNumberNext = $(this).val().split("-")[1];
	var currentPanel = '#panel-' + panelNumberCurrent + '-content'
	var nextPanel = '#panel-' + panelNumberNext + '-content'
	console.log(panelNumberCurrent, panelNumberNext);
	console.log(currentPanel, nextPanel);

	$(currentPanel).fadeOut(150, function() {
		$(currentPanel).removeClass('active');
		$(currentPanel).addClass('inactive');
		$(nextPanel).fadeIn(150, function () {
			$(nextPanel).removeClass('inactive');
			$(nextPanel).addClass('active');
		});

	});

});


$(document).on('click', '#form-submit', function(e) {
	var one = $('input[name=one]:checked').val();
	var two = $('input[name=two]:checked').val();
	var three = $('input[name=three]:checked').val();
	var four = $('input[name=four]:checked').val();
	var five = $('input[name=five]:checked').val();
	var six = $('input[name=six]:checked').val();

	console.log(one, two, three, four, five, six);

});