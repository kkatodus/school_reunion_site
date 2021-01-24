var modalBtn = document.querySelector(".modal-btn");
var modalBg = document.querySelector(".modal-bg");
var modalClose = document.querySelector(".modal-close")

modalBtn.addEventListener("click",function(){
    modalBg.classList.add("createpost_active");
})

modalClose.addEventListener("click",function(){
    modalBg.classList.remove("createpost_active")
})