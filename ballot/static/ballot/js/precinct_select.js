$(document).ready(function() {
    $("select#id_precinct_area").change(function() {
        if ($(this).val() == '') {
            $("select#id_precinct").attr('disabled', true);
            $("#submit-id-submit").attr('disabled', true);
        } else {
            $("select#id_precinct").attr('disabled', false);
            get_prec_options();
        };
    });
    $("select#id_precinct").change(function(vent) {
        if ($(this).val() == '') {
            return;
        }
        $("#submit-id-submit").attr('disabled', false);
    });
});

function get_prec_options() {
    $.ajax({
        url: "/ballot/prec_options/" + $('select#id_precinct_area').val()
    }).done(function(data) {
        $("select#id_precinct").html(data)
    });
};