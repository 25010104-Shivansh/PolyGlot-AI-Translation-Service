async function performTranslation() {
    const text = document.getElementById('inputText').value;
    const source = document.getElementById('sourceLang').value;
    const target = document.getElementById('targetLang').value;
    const output = document.getElementById('resultText');

    if (!text) {
        alert("Please enter some text first.");
        return;
    }

    output.innerText = "Translating...";
    output.style.opacity = "0.5";

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text, source: source, target: target })
        });

        const data = await response.json();
        
        output.style.opacity = "1";
        if(data.status === 'success') {
            output.innerText = data.translation;
        } else {
            output.innerText = "Error: " + data.message;
        }
    } catch (error) {
        output.innerText = "Network Error: Ensure the server is running.";
    }
}

function copyToClipboard() {
    const text = document.getElementById('resultText').innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("Translation copied!");
    });
}

// --- Dark Mode Logic ---
const checkbox = document.getElementById('checkbox');

checkbox.addEventListener('change', () => {
    document.body.classList.toggle('dark');
});

// NOTE: Character counter logic removed as requested.