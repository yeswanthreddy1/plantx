document.addEventListener('DOMContentLoaded', () => {
    // Top-Level Screens
    const landingScreen = document.getElementById('landing-screen');
    const appContainer = document.getElementById('app-container');
    const btnGetStarted = document.getElementById('btn-get-started');

    // Left Panel Elements (Upload & Preview)
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const btnRemove = document.getElementById('btn-remove');
    const btnAnalyze = document.getElementById('btn-analyze');

    // Right Panel Elements (Analysis & Results)
    const emptyState = document.getElementById('empty-state');
    const loader = document.getElementById('loader');
    const resultsContent = document.getElementById('results-content');
    const errorBanner = document.getElementById('error-banner');
    
    // Result Data Elements
    const diseaseName = document.getElementById('disease-name');
    const confidenceFill = document.getElementById('confidence-fill');
    const confidenceText = document.getElementById('confidence-text');
    const treatmentText = document.getElementById('treatment-text');
    const btnNewScan = document.getElementById('btn-new-scan');

    let currentFile = null;

    // --- State Management --- 

    function resetRightPanel() {
        emptyState.classList.remove('hidden');
        loader.classList.add('hidden');
        resultsContent.classList.add('hidden');
        hideError();
    }

    // --- Get Started Transition ---
    btnGetStarted.addEventListener('click', () => {
        landingScreen.classList.add('hidden');
        appContainer.classList.remove('hidden');
    });

    // --- Drag and Drop functionality ---

    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('drop-zone--over');
    });

    ['dragleave', 'dragend'].forEach(type => {
        dropZone.addEventListener(type, () => {
            dropZone.classList.remove('drop-zone--over');
        });
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('drop-zone--over');

        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length) {
            handleFileUpload(fileInput.files[0]);
        }
    });

    // --- File Handling UI ---

    function handleFileUpload(file) {
        if (!file.type.startsWith('image/')) {
            showError('Please upload an image file (JPEG or PNG).');
            return;
        }

        currentFile = file;
        resetRightPanel(); // Clear previous results when new file is uploaded
        
        // Show preview on the left panel
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            imagePreview.src = reader.result;
            dropZone.classList.add('hidden');
            previewContainer.classList.remove('hidden');
        };
    }

    btnRemove.addEventListener('click', () => {
        currentFile = null;
        fileInput.value = '';
        previewContainer.classList.add('hidden');
        dropZone.classList.remove('hidden');
        resetRightPanel(); // Go back to original empty state on right
    });

    btnNewScan.addEventListener('click', () => {
        btnRemove.click();
    });

    // --- Analysis Logic ---

    btnAnalyze.addEventListener('click', async () => {
        if (!currentFile) return;

        // UI State: Right Panel Loading (Left panel stays with image preview!)
        emptyState.classList.add('hidden');
        resultsContent.classList.add('hidden');
        loader.classList.remove('hidden');
        hideError();

        // Prepare FormData
        const formData = new FormData();
        formData.append('file', currentFile);

        try {
            // API Call
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Something went wrong during prediction.');
            }

            // UI State: Right Panel Success
            displayResults(data);

        } catch (err) {
            // UI State: Right Panel Error
            loader.classList.add('hidden');
            emptyState.classList.remove('hidden'); // Fallback purely visual
            showError(err.message);
        }
    });

    function displayResults(data) {
        loader.classList.add('hidden');
        resultsContent.classList.remove('hidden');

        diseaseName.textContent = data.disease;
        treatmentText.textContent = data.treatment;
        confidenceText.textContent = data.confidence;
        
        // Check health status to style accordingly
        if (data.original_label && data.original_label.toLowerCase().includes('healthy')) {
            diseaseName.style.color = 'var(--primary-color)';
        } else {
            diseaseName.style.color = 'var(--warning)';
        }

        // Animate fill bar
        setTimeout(() => {
            confidenceFill.style.width = data.confidence;
            
            // Color based on confidence
            if (data.raw_confidence < 60) {
                confidenceFill.style.background = 'linear-gradient(90deg, #ef4444, #f87171)';
            } else if (data.raw_confidence < 80) {
                confidenceFill.style.background = 'linear-gradient(90deg, #f59e0b, #fbbf24)';
            } else {
                confidenceFill.style.background = 'linear-gradient(90deg, #27ae60, #2ecc71)';
            }
        }, 100);
    }

    function showError(msg) {
        errorBanner.textContent = msg;
        errorBanner.classList.remove('hidden');
    }

    function hideError() {
        errorBanner.classList.add('hidden');
    }
});
