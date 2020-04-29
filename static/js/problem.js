initQuestionHandler = function () {

    var clicks = 0;

    // function to convert JSON into OpenFST representation
    document.getElementById("printFSM").onclick =
        function () {

            // if button has been clicked more than 5 times,
            // reveal solution
            clicks += 1;
            if (clicks == 5) {
                document.getElementById('view-sol').style.display = 'inline';
            }

            output('Processing submission...', 'Please wait...');

            // Store JSON data in a JS variable
            var fsm = sessionStorage['fsm'];

            var problem_data = $('#my-data').data();

            $.ajax({
                type: "POST",
                url: "/submit",
                data: {
                    fsm_json: fsm,
                    probid: problem_data.probid,
                    deterministic: problem_data.det
                },
                success: callbackFunc
            })
        };
}

function callbackFunc(response) {

    var res = JSON.parse(response);
    title = res.title;
    message = res.message;

    hint = '<br><span class="term">Hint:</span> ';
    if (res.hasOwnProperty('hint'))
    {
        hint += res.hint;
        message += hint;
        output(title, message);
        return;
    }

    if (res.hasOwnProperty('solution_fsm') &&
        res.hasOwnProperty('student_fsm'))
        {
        solution_fsm = noam.fsm.parseFsmFromString(res.solution_fsm);
        student_fsm = noam.fsm.parseFsmFromString(res.student_fsm);
        console.log(res.solution_fsm);
        console.log(res.student_fsm)

        sol_minus_stud = noam.fsm.difference(solution_fsm, student_fsm);
        example_string = noam.fsm.randomStringInLanguage(sol_minus_stud);

        if (output_diff_hint(solution_fsm, student_fsm, true) == 0) return;
        if (output_diff_hint(student_fsm, solution_fsm, false) == 0) return;

        hint += 'This hint shouldn\'t look like this'
        message = message + hint;
    }

    // output title and message
    output(title, message);
}


function output_diff_hint(fsm1, fsm2, sol_first) {

    // compute difference L(FSM1) - L(FSM2) and generate string
    difference = noam.fsm.difference(fsm1, fsm2);
    example_string = noam.fsm.randomStringInLanguage(difference);

    // if null, no strings in the language
    if (example_string == null) {
        return -1;
    }

    tries = 0
    while (tries < 1000 && example_string.length > 8) {
        example_string = noam.fsm.randomStringInLanguage(difference);
        tries += 1;
    }

    example_string = example_string.join("");

    // if example string is empty, print epsilon
    if (example_string.trim() == '') {
        example_string = '\\varepsilon'
    }

    // encapsulate in math span
    example_string = '<span class="math-color">\\(' + example_string +
        '\\)</span>'

    // display correct hint, depending on order of difference
    if (sol_first) {
        hint += 'Consider the string ' + example_string + '. Your machine should' +
            ' <span class="text-success" style="font-weight:bold">accept</span> ' +
            'this string, but it <span class="text-danger" ' + 
            'style="font-weight:bold">rejects</span> it.';
    }
    else {
        hint += 'Consider the string ' + example_string + '. Your machine should' +
            ' <span class="text-danger" style="font-weight:bold">reject</span> ' +
            'this string, but it <span class="text-success" ' + 
            'style="font-weight:bold">accepts</span> it.';
    }

    // append hint to message and output title and message
    message = message + hint;
    output(title, message);

    return 0;
}