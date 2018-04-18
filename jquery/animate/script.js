$(function () {
    // 显示 隐藏 toggle
    $("#t_show").click(function () {
        $("#img1").show();
    });
    $("#t_hide").click(function () {
        $("#img1").hide();
    });
    $("#t_toggle").click(function () {
        $("#img1").toggle();
    });

    // 向上 向下 slidetoggle
    $("#t_slideUp").click(function () {
        $("#img1").slideUp();
    });
    $("#t_slideDown").click(function () {
        $("#img1").slideDown();
    });
    $("#t_slideToggle").click(function () {
        $("#img1").slideToggle();
    });

    // fade in out toggle to
    $("#t_fadeIn").click(function () {
        $("#img1").fadeIn();
    });
    $("#t_fadeOut").click(function () {
        $("#img1").fadeOut();
    });
    $("#t_fadeToggle").click(function () {
        $("#img1").fadeToggle();
    });
    $("#t_fadeTo").click(function () {
        $("#img1").fadeTo("slow",0.5);
    });
    // animate
    $("#t_animate").click(function () {
        $(".img2 img").animate({height:"100px",opacity:"0.2"},"2000");
    });
});