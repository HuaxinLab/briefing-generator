window.onload = function() {
    // tab control
    let briefingDiv = document.getElementById("briefing");
    var typeBtn = briefingDiv.getElementsByTagName("input");
    var postsDiv = briefingDiv.getElementsByClassName("posts");

    for(var i = 0; i < typeBtn.length; i++){
        typeBtn[i].index = i;
        typeBtn[i].onclick = function() {
            for(var i = 0; i < typeBtn.length; i++){
                typeBtn[i].className = "";
                postsDiv[i].style.display = "none";
            }
            this.className = "active";
            postsDiv[this.index].style.display = "block";
        };
    }
};