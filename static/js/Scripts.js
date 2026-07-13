document.addEventListener("DOMContentLoaded", function () {

    const fileInput = document.getElementById("file");
    const form = document.getElementById("uploadForm");
    const previewImage = document.getElementById("previewImage");
    const uploadBox = document.querySelector(".upload-box");
    const loadingModal = document.getElementById("loadingModal");

    // Helper: validate + preview a given File object
    function handleFile(file) {

        if (!file) return false;

        if (!file.type.startsWith("image/")) {
            alert("Please select an image file.");
            return false;
        }

        if (previewImage) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        return true;
    }

    // Image Preview (file picker)
    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];
            if (!file) return;

            if (!handleFile(file)) {
                this.value = "";
            }
        });
    }

    // Show loading spinner when form is submitted
    if (form) {
        form.addEventListener("submit", function (e) {

            if (!fileInput || fileInput.files.length === 0) {
                e.preventDefault();
                alert("Please select an MRI image.");
                return;
            }

            if (loadingModal) {
                const modal = new bootstrap.Modal(loadingModal);
                modal.show();
            }
            // no preventDefault here -> form submits normally to Flask
        });
    }

    // Drag & Drop
    if (uploadBox) {

        uploadBox.addEventListener("dragover", function (e) {
            e.preventDefault(); // required, or drop never fires
            uploadBox.style.background = "#eaf4ff";
            uploadBox.style.borderColor = "#0d6efd";
        });

        uploadBox.addEventListener("dragleave", function (e) {
            e.preventDefault();
            uploadBox.style.background = "#f8fbff";
            uploadBox.style.borderColor = "#0d6efd";
        });

        uploadBox.addEventListener("drop", function (e) {
            e.preventDefault();
            uploadBox.style.background = "#f8fbff";

            const file = e.dataTransfer.files[0];
            if (!file || !fileInput) return;

            if (handleFile(file)) {
                // Assign the dropped file to the actual <input type="file">
                // so the form submits it correctly
                fileInput.files = e.dataTransfer.files;
            }
        });

    }

});