function previewImage() {
    var preview = document.getElementById('preview-img');
    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0];

    if (file) {
        var reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    } else {
        preview.src = '';
    }
}