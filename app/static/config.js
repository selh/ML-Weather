Dropzone.autoDiscover = false;

$(function() {
  var myDropzone = new Dropzone("#my-dropzone", {url: "file/post"});

  myDropzone.on("addedfile", function(file) {
    file.previewElement.addEventListener("click", function() {
      myDropzone.removeFile(file);
    });
  });

  myDropzone.on("success", function(file) {
    window.location = "{{ url_for('prediction') }}"
  });

  myDropzone.on("success", function () {
    if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
        window.location.reload();
    }

  });
})