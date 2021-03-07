var inputs = $.makeArray($(".pic_input"));
var newest_input = inputs[inputs.length - 1];


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
    var new_input = $("<input>").attr({"type":"file",
                                       "name":"image",
                                       "accept":"image/*",
                                       "class":"not_first_pic_input pic_input"})
    $("#act_pic_inputs").append(new_input);
    newest_input = new_input;
})

$("#pic_preview").on("click",function(){
    newest_input.click();
})


$(newest_input).on("change",function(){
    if (newest_input.files && newest_input.files[0]){
        var post_pic_file = newest_input.files[0];
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
