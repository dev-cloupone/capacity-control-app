// Function to handle file drop
function handleFileDrop(event) {
    event.preventDefault();
    event.stopPropagation();

    // Add hover effect
    event.target.classList.remove('hover');

    // Access dropped files
    const files = event.dataTransfer.files;

    // If files exist, update file input and display file name
    if (files.length > 0) {
        const fileInput = document.getElementById('csv_file');
        fileInput.files = files;

        // Update label to show file name and display submit button
        updateFileNameAndButtonVisibility();
    }
}

// Function to handle file drag over
function handleDragOver(event) {
    event.preventDefault();
    event.stopPropagation();

    // Add hover effect
    event.target.classList.add('hover');
}

// Function to handle file drag leave
function handleDragLeave(event) {
    event.preventDefault();
    event.stopPropagation();

    // Remove hover effect
    event.target.classList.remove('hover');
}

// Update label to display file name and show submit button if a file is selected
function updateFileNameAndButtonVisibility() {
    const fileInput = document.getElementById('csv_file');
    const label = document.getElementById('csv_label');
    const submitBtn = document.getElementById('submitBtn');

    if (fileInput.files.length > 0) {
        label.innerText = fileInput.files[0].name;
        submitBtn.style.display = 'block'; // Show submit button
    } else {
        label.innerText = "Ou selecione manualmente:";
        submitBtn.style.display = 'none'; // Hide submit button if no file selected
    }
}

// Event listeners for drag and drop functionality
const dropZone = document.getElementById('dropZone');

dropZone.addEventListener('dragover', handleDragOver);
dropZone.addEventListener('dragleave', handleDragLeave);
dropZone.addEventListener('drop', handleFileDrop);

// Additional event listener for file input change
const fileInput = document.getElementById('csv_file');
fileInput.addEventListener('change', updateFileNameAndButtonVisibility);
