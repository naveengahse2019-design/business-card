let myRate = document.querySelectorAll("button")[0]

function updateDisplay(){

    const gold = document.getElementById("gold-rate").innerHTML
    const silver = document.getElementById("silver-rate").innerHTML

    document.getElementById("gold-rate").innerText = "₹"+gold
    document.getElementById("silver-rate").innerText = "₹"+silver
}

myRate.addEventListener("click", async () => {

    try{

        const res = await fetch("/rates/")
        const data = await res.json()

        document.getElementById("gold-rate").innerHTML = data.gold
        document.getElementById("silver-rate").innerHTML = data.silver

        updateDisplay()

        // update time after fetching
        updateDateTime()

    }
    catch(err){
        console.log("Error fetching rates", err)
    }

})
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

function generateImage(){

const card = document.getElementById("card");

html2canvas(card,{
scale:1
}).then(canvas=>{
const link=document.createElement("a");
link.download="gold-rate.png";
link.href=canvas.toDataURL();
link.click();
});

}
