$(document).ready(function(){
    // $.material.init();
    $('body').bootstrapMaterialDesign();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $("#register-form").serialize();
        $.ajax({
            url: "/signup",
            type: "POST",
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });
});