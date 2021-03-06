$("#vis_upload_container").on("click", function(){
    $("#profile_picture_input").click();
})

$("#profile_picture_input").on("change", function(){
    if (this.files && this.files[0]){
        var profile_pic_file = this.files[0];
        var file_reader = new FileReader();
        file_reader.onload = function(e){
            $("#vis_upload_input").css({"background-image":"url("+e.target.result+")","background-size":"100%","background-repeat":"no-repeat"})
        }
        file_reader.readAsDataURL(profile_pic_file);
    }
})