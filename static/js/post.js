var modalBtn = document.querySelector(".modal-btn");
var modalBg = document.querySelector(".modal-bg");
var modalClose = document.querySelector(".modal-close")
var postCreationForm = document.getElementById("post_creation")

modalBtn.addEventListener("click",function(){
    modalBg.classList.add("createpost_active");
})

modalClose.addEventListener("click",function(){
    modalBg.classList.remove("createpost_active")
})

function addPostPicture(){
    var new_photo_input = document.createElement("input")
    new_photo_input.name ="image"
    new_photo_input.type = "file"
    postCreationForm.appendChild(new_photo_input)

}

