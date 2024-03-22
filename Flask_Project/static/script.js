document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('camera');

    // Check if the browser supports the getUserMedia API
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                // Assign the stream to the video element
                video.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing the camera:', error);
            });
    } else {
        console.error('getUserMedia is not supported in this browser');
    }
});
