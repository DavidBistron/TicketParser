// Function for text analyzing
function analyzeText() {
    let text = document.getElementById('inputText').value;

    // If file is uploaded, read the content
    if (document.getElementById('fileUpload').files.length > 0) {
        const file = document.getElementById('fileUpload').files[0];
        const reader = new FileReader();
        reader.onload = function(event) {
            text = event.target.result;
            sendRequest(text);
        };
        reader.readAsText(file);
    } else {
        sendRequest(text);
    }
}

// Function to send request and generate output (Name, Info, Products, Sentiment Analysis)
function sendRequest(text) {
    fetch('/analyze', {
        method: 'POST',
        body: new URLSearchParams({ text: text }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })
    .then(response => response.json())
    .then(data => {
        // Display results
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p><strong>Customer Name:</strong> ${data.customer_name}</p>
            <p><strong>Contact Info:</strong> ${data.contact_info}</p>
            <p><strong>Purchased Products:</strong> ${data.products.join(', ')}</p>
            <p><strong>Content of Email:</strong> ${data.filtered_text}</p> 
            <div><strong>Sentiment:</strong> 
                <div class="sentiment ${data.sentiment_color}"></div>
            </div>
        `;
    })
    .catch(error => console.error('Error:', error));
}

// Function for removing the uploaded file and resetting the text field 
function removeFile() {
    // Empty file input field
    document.getElementById('fileUpload').value = "";
    
    // Empty text-area field
    document.getElementById('inputText').value = "";

    // Remove displayed content in the result display
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
}