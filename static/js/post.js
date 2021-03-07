$(".modal-btn").on("click", function(){
    $(".modal-bg").addClass("createpost_active");
})

$(".modal-close").on("click",function(){
    $(".modal-bg").removeClass("createpost_active")
})

$("#picture_add_button").on("click",function(){
    var new_input = $("<input>").attr({"type":"file","name":"image"})
    $("#post_creation").append(new_input)
})


