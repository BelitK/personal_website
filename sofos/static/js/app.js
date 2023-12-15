let scanner = new Instascan.Scanner({ video: document.getElementById('scanner') });

scanner.addListener('scan', function (content) {
    // Send QR data to Flask backend
    $.ajax({
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        url: '/process',
        data: JSON.stringify({ qr_data: content }),
        success: function (response) {
            // Update the result text element
            $('#renum').val(response.renum);
            $('#result').text(response.message);
        }
    });
});

// Start the scanner
Instascan.Camera.getCameras().then(function (cameras) {
    if (cameras.length > 0) {
        var selectedCam = cameras[0];
        $.each(cameras, (i, c) => {
            if (c.name.indexOf('back') !== -1) {
                selectedCam = c;
                return false;
            }
        });

        scanner.start(selectedCam);
    }
}).catch(function (e) {
    console.error(e);
});

