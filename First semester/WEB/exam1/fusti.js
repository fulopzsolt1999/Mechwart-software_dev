function mouseOver(img) {
    document.getElementById(img).style.width = "400px";
    document.getElementById(img).addEventListener("mouseout", function (){
        document.getElementById(img).style.width = "";
    })
}