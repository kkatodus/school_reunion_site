var newest_input = $("#newest_pic_input")


$(".modal-btn").on("click", function(){
    $(".modal-bg").addClass("createpost_active");
})

$(".modal-close").on("click",function(){
    $(".modal-bg").removeClass("createpost_active")
    var delete_list =$.makeArray($("#post_creation").children(".not_first_pic_input"))
    delete_list.forEach(item=>{
        item.remove();
    })
    
})

$("#picture_add_button").on("click",function(){
    $("#newest_pic_input").removeAttr("id"); 
    var new_input = $("<input>").attr({"type":"file",
                                       "name":"image",
                                       "accept":"image/*",
                                       "class":"not_first_pic_input pic_input",
                                       "id":"newest_pic_input"})                                
    $("#act_pic_inputs").append(new_input);

})

$("#pic_preview").on("click",function(){
    $("#newest_pic_input").click();
    $("#newest_pic_input").on("change",function(){
        console.log("newestinput changed")
        if (this.files && this.files[0]){
            var post_pic_file = this.files[0];
            var file_reader = new FileReader();
            file_reader.onload = function(e){
                $("#pic_preview").css({"background-image":"url("+e.target.result+")"});
                $("#pic_preview>h2").hide();
                setTimeout(function(){
                    var past_pic = $("<div></div>").css({"height":"80%",
                                                     "width":"50px",
                                                     "background-image":"url("+e.target.result+")",
                                                     "background-position":"center center",
                                                     "background-size":"cover",
                                                     "border-radius":"10%"})
                    $("#other_pics").append(past_pic);
                    $("#pic_preview").css({"background-image":"none"});
                    $("#pic_preview>h2").show();
                    $("#picture_add_button").click();
                },2000);
                
            }
            file_reader.readAsDataURL(post_pic_file)
        }
    })
})

