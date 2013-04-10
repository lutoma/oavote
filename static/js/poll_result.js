$(document).ready(function() {

	$('.plot-pie').each(function(i, plot) {

		var data = [
			{
				label: "Dafür",
				data: $(plot).data('yes'),
				color: '#EDC240'
			}, {
				label: "Dagegen",
				data: $(plot).data('no'),
				color: '#CB4B4B'
			}, {
				label: "Enthaltung",
				data: $(plot).data('abst'),
				color: '#AFD8F8'
			}
		];

		var options = {
			series: {
				pie: { show: true }
			},

			legend: {
				show: true,
				labelFormatter: function(label, series) {
					return label + ': ' + Math.round(series.percent) + '%';
				}
			}
		};

		$.plot(plot, data, options); 

	})
})