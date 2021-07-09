$(document).on('click', '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});

var PembayaranChart = (function() {

    // Variables
  
    var $chart = $('#chart-pembayaran');
    var pembayaranList = document.getElementsByClassName('pembayaran-list');
    var newPembayaranlist = []
    for(let item of pembayaranList){
        newPembayaranlist.push(item.textContent);
    }
  
  
    // Methods
  
    function init($chart) {
      var PembayaranChart = new Chart($chart, {
        type: 'line',
        options: {
          scales: {
            yAxes: [{
              gridLines: {
                lineWidth: 1,
                color: Charts.colors.gray[900],
                zeroLineColor: Charts.colors.gray[900]
              },
              ticks: {
                callback: function(value) {
                  if (!(value % 10)) {
                    return value;
                  }
                }
              }
            }]
          },
          tooltips: {
            callbacks: {
              label: function(item, data) {
                var label = data.datasets[item.datasetIndex].label || '';
                var yLabel = item.yLabel;
                var content = '';
  
                if (data.datasets.length > 1) {
                  content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                }
  
                content += '<span class="popover-body-value">' + yLabel + '</span>';
                return content;
              }
            }
          }
        },
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
          datasets: [{
            label: 'Performance',
            data: newPembayaranlist
          }]
        }
      });
  
      // Save to jQuery object
  
      $chart.data('chart', PembayaranChart);
  
    };
  
  
    // Events
  
    if ($chart.length) {
      init($chart);
    }
  
  })();

// $("#status-pembayaran-form").hide();