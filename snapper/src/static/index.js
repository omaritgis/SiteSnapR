
// display image fetched from server
async function displayImage() {
    const xml = new XMLHttpRequest();
    xml.open('GET', image, true);
    const img = document.createElement('img');
    img.src = image;
    document.body.appendChild(img);
}