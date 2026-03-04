function updateDateTime() {
    const now = new Date();

    const formatted = now.toLocaleString("ta-IN", {
        day: "2-digit",
        month: "long",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        hour12: true
    });

    document.getElementById("datetime").innerText = formatted;
    
}


function generateImage() {
    html2canvas(document.querySelector("#card")).then(canvas => {

        // Convert canvas to JPEG
        const image = canvas.toDataURL("image/jpeg", 1.0);

        // Create download link
        const link = document.createElement("a");
        link.href = image;
        link.download = "gold-rate.jpeg";

        link.click();
    });
}