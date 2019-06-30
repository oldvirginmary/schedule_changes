'use strict';


(function (window, document, $) {
    $(document).ready(function () {
        $('#groupNumberField').dropdown();

        $('#historyBtn').click(function() {
            var group_number = $('#groupNumberField').val();

            var request = $.ajax({
                url: 'http://127.0.0.1:8000/publication_date/',
                method: 'POST',
                dataType: 'text',
                data: {
                    group_number: group_number,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
            });

            request.done(function(data, textStatus, jqXHR) {
                var data = JSON.parse(data);
                var mainSection = $('#main_section');

                if ($('#dayField').text() && $('#timeField').text()){
                    $('#dayField').text(data['day']);
                    $('#timeField').text(data['time']);
                } else {
                    var day = $('<p>').attr('id', 'dayField').text(data['day']);
                    var time = $('<p>').attr('id', 'timeField').text(data['time']);

                    mainSection.append(day);
                    mainSection.append(time);
                }
            });

            request.fail(function(jqXHR, textStatus, errorThrown) {
                alert('fail');
            });
        });

        $('#downloadBtn').click(function () {
            var group_number = $('#groupNumberField').val();

            var request = $.ajax({
                url: 'http://127.0.0.1:8000/',
                method: 'POST',
                dataType: 'text',
                data: {
                    group_number: group_number,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
            });

            request.done(function(data, textStatus, jqXHR) {
                console.log('done');
            });

            request.fail(function(jqXHR, textStatus, errorThrown) {
                console.log('fail');
            });
        });
    });
})(window, document, jQuery);
