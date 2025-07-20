const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

async function uploadChat() {
    const input = document.getElementById('botInput');
    const output = document.getElementById('jsonOutput');
    const copyWrapper = document.getElementById('copyWrapper');
    const file = input.files[0];

    if (!file) {
        alert('Please select a file (Text)');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    output.classList.remove('hidden');
    output.textContent = 'Extracting Chat...';
    copyWrapper.classList.add('hidden');

    try {
        const response = await fetch(`${API_BASE_URL}/upload-file`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to extract chat.');
        }

        const result = await response.json();
        output.textContent = JSON.stringify(result, null, 2);
        copyWrapper.classList.remove('hidden');
    } catch (error) {
        output.textContent = `Error: ${error.message}`;
    }
}

function copyJSON() {
    const jsonOutput = document.getElementById("jsonOutput").innerText;
    const copyButton = document.getElementById("copyButton");

    navigator.clipboard.writeText(jsonOutput).then(() => {
        const originalText = copyButton.innerHTML;

        copyButton.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            Copied!
        `;

        setTimeout(() => {
            copyButton.innerHTML = originalText;
        }, 2000);
    });
}

