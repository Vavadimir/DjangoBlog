/**
 * Created by vavadimir on 8/28/17.
 */
$(document).ready(function() {
    var form = $('#form-cmnt');
    console.log(form);
    var pathname = window.location.pathname;

    form.on('submit', function(e){
        e.preventDefault();
        var data = {};
        var path = pathname.replace('/', '');
        path = path.replace('/', '');
        console.log(path);
        data.comm = $('#input-cmnt').val();
        data.path = path;
        var csrf_token = $('#form-cmnt [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        console.log('gggg');
        $.ajax({
             url: '../../postproc',
             type: 'POST',
             data: data,
             cache: true,
             success: function () {
                 console.log("OK");
                 $('#input-cmnt').val('');
                 getMessages();
             },
             error: function() {
                 console.log("ERROR");
             }
             });
    });
        function getMessages(){
            var path = pathname.replace('/', '');
            path = path.replace('/', '');
            var data = {};
            data.path = path;
            var csrf_token = $('#form-cmnt [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
             url: '../../comments',
             type: 'POST',
             data: data,
             cache: true,
             success: function (messages) {
                 console.log("OK");
                 $('#cmnts').html(messages);
             },
             error: function() {
                 console.log("ERROR");
             }
             });
        // $.get('../../comments', function(messages) {
        //     $('#cmnts').html(messages);
        // });
    }

    setInterval(getMessages, 2000);
});