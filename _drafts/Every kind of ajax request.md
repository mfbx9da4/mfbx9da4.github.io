Every kind of ajax request
Post form/upload cross origin

    var processResponse = function (data) {
    var formData = new FormData();    
    formData.append('key', data.key);
    formData.append('AWSAccessKeyId', data.AWSAccessKeyId);
    formData.append('acl', 'public-read');
    formData.append('policy', data.policy);
    formData.append('signature', data.signature);
    formData.append('success_action_status', "201");
    formData.append('Content-Type', data.contentType);
    formData.append('file', $('#file')[0].files[0]);


    $.ajax({
        url: "http://aedeveloper.s3.amazonaws.com/",
        type: "POST",
        processData: false,
        contentType: false,
        data: formData,
        dataType: 'text', // must be text if xml is returned
        success: onPosted,
        error: function(res, status, error) {
            throw error;
        }
    });
};
Simple get

    $.ajax({
        url: "/signed",
        data: {title: filename },
        type: "GET",
        dataType: "json",
        success: processResponse,
        error: function(res, status, error) {
            throw error;
        }
    });
