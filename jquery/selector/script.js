$(document).ready(function () {
    // id选择器
    $("#sp1").click(function () {
        $("#id1").toggleClass("red");
    });
    $("#sp2").click(function () {
        $("#id2").toggleClass("red");
    });
    $("#sp3").click(function () {
        $("#id3").toggleClass("red");
    });
    // class选择器
    $("#sp4").click(function () {
        $(".class1").toggleClass("red");
    });
    $("#sp5").click(function () {
        $(".class2").toggleClass("red");
    });
    //元素选择器
    $("#sp6").click(function () {
        $("span").toggleClass("red");
    });
    //组合选择器
    //并列选择器
    $("#sp7").click(function () {
        $("#id1,#id2,#id3").toggleClass("red");
    });
    //家族
    $("#sp10").click(function () {
        $("ul span").toggleClass("red");
    });

});