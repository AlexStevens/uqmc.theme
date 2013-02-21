$( function() {
    $('#portal-logo a').on('click', function(e) {
        e.preventDefault();
        var logo = $(this.id + ' span.last');
        if (logo.text() == 'C') {
            $('#portal-logo a span.first').animate({'padding-right': '0.1em'}, 'slow');
            logo.animate({width: 'toggle'}, 'slow', function() {
                $(this).text('ountain Club');
            });
            logo.animate({width: 'toggle'}, 'slow');
        } else {
            $('#portal-logo a span.first').animate({'padding-right': '0'}, 'slow');
            logo.animate({width: 'toggle'}, 'slow', function() {
                $(this).text('C');
            });
            logo.animate({width: 'toggle'}, 'slow');
        }
    });
});
