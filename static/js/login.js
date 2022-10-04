$(document).on('click', '.toggle', function() { 
        $('.formulario').animate({
            height: "toggle",
            'padding-top': 'toggle',
            'padding-bottom': 'toggle',
            opacity: 'toggle'
        }, "slow");
});


