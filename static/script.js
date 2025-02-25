const imageInput = document.getElementById('imageInput');
const previewContainer = document.getElementById('previewContainer');
const previewText = document.getElementById('previewText');
const recommendationResults = document.getElementById("recommendation-results");

imageInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.alt = file.name;
            previewContainer.innerHTML = '';
            previewContainer.appendChild(img);
        }

        reader.readAsDataURL(file);
    } else {
        previewContainer.innerHTML = '<span id="previewText">No image selected</span>';
    }
});

function uploadImage() {
    const file = imageInput.files[0];
    if (!file) {
        alert("Please select an image first.");
        return;
    }

    const formData = new FormData();
    formData.append('photo', file); // Use 'photo' to match your app.py

    fetch('/analyze', { // Match your app.py endpoint
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        recommendationResults.innerHTML = "<h2>Recommended Songs:</h2>";

        if (data.songs && Array.isArray(data.songs)) {
            const ul = document.createElement('ul');
            data.songs.forEach(song => {
                const li = document.createElement('li');
                li.textContent = `${song.name} - ${song.artist}`;
                ul.appendChild(li);
            });
            recommendationResults.appendChild(ul);
        } else {
            recommendationResults.innerHTML += "<p>No recommendations found or invalid data received.</p>";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        recommendationResults.innerHTML = "<p>Error getting recommendations. Please try again later.</p>";
    });
}