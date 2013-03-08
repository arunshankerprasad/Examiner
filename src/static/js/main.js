$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};




function saveQuestion(e) {
    var prv_text = $(".save_question_button").html();
    $(".save_question_button").html('Please wait...');
    if(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    var data = Array();
    $("#questionaire_container_form form").each(function (i, f) {
        data.push($(f).serializeObject());
    });
    $.ajax({
            url: "/questionaire/save",
            dataType: "json",
            type: "POST",
            data: JSON.stringify(data)

        }).done(function (data) {
            $(".save_question_button").html(prv_text);
            if (data.is_success) {
                $("#questionaire_container_form").html($('<h2>Your questionaire has been posted!</h2>\
                   <br><button id="review_answers_button" class="review_answers_button">Review the responses</button>'));
                $(".review_answers_button").click(reviewResponses);
            } else {
                $(data.errors).each(function (i, error) {
                    $(error.errors).each(function (k, er) {
                        $("#" + error.form + " #" + k).html(er);
                    });
                });
            }
    });
}

PRV_COUNT = 1;

function addAnotherQuestion(e) {
    var n_e = $('<div class="form">' + $('div#question_set_0').html() + '</div>');
    n_e.addClass('new');
    n_e.attr({'id': 'form_' + PRV_COUNT ++});
    $("#save_question").append(n_e);
    // trigger on focus on newly created div
    n_e.focus();
    n_e.removeClass('new');
}

function reviewResponses() {
    $(this).remove();
    $.get('/questionaire/responses', {}, function(responses) {
        if(responses.length > 0) {
            $('div#responses').html('');
            $(responses).each(function (i, answer){
                var html = '<div class="container"><form action="#" class="responses_form"><div class="responses">\
                <input type="hidden" value="' + answer.key + '">\
                <span class="fl question">' + answer.question_text + '</span>\
                <span class="fl answer">Answer<br>' + answer.text + '</span><br>\
                <span class="fl answer">By<br>' + answer.answered_by + '</span><br>\
                <div></div></form>';

                if (! answer.is_evaluated) {
                    html += '<button class="correct_answer_button">Correct</button>\
                    <button class="wrong_answer_button">Wrong</button>';
                } else {
                    if (answer.is_correct) {
                        html += '<br><br><span>Correct</span>';
                    } else {
                        html += '<br><br><span>Wrong</span>';
                    }
                }
                $('div#responses').append(html);

                var func = function (e, that, is_correct) {
                    var prv_text = that.html();
                    that.html('Please wait...');
                    $.ajax({
                            url: "/answer/evaluate",
                            dataType: "json",
                            type: "POST",
                            data: JSON.stringify({is_correct: is_correct, 'key': $(that.parents('.responses').children()[0]).val()})
                        }).done(function (data) {
                            that.html(prv_text);
                            var html = '<div class="responses">\
                            <span class="fl question">' + answer.question_text + '</span>\
                            <span class="fl answer">Answer<br>' + answer.text + '</span><br>\
                            <span class="fl answer">By<br>' + answer.answered_by + '</span><br>';
                            $('div#responses').html('').append(html);
                            that.prev('div.container').html(html);
                    });
                };
                $('.correct_answer_button').click(function (e) {func(e, $(this), true)});
                $('.wrong_answer_button').click(function (e) {func(e, $(this), false)});
            });
        } else {
            $('div#responses').html('<h4>No responses</h4>');
        }
    }, 'json');
}

function saveResponse(e) {
    var prv_text = $(".save_answer_button").html();
    $(".save_answer_button").html('Please wait...');
    var data = Array();
    $("form.save_answer_form").each(function (i, f) {
        data.push($(f).serializeObject());
    });
    $.ajax({
            url: "/answers/save",
            dataType: "json",
            type: "POST",
            data: JSON.stringify(data)

        }).done(function (data) {
            $(".save_answer_button").html(prv_text);
            if (data.is_success) {
                $("#container_form").html($('<h2>Your response has been posted!</h2>'));
                $(".review_answers_button").click(reviewResponses);
            } else {
                $(data.errors).each(function (i, error) {
                    $(error.errors).each(function (k, er) {
                        $("#" + error.form + " #" + k).html(er);
                    });
                });
            }
    });
}
