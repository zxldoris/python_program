$(function () {
    $("#click1").click(function () {
        alert(1);
    });
    //hover里面有两个函数参数，第一个是进入，第二个是离开
    $("#hover1").hover(function () {
        alert("进入");
    },function () {
        alert("离开");
    });
    $("#input1").blur(function () {
        alert("blur");
    });
    $("#input1").focus(function () {
        alert("focus");
    });

    // 推荐
    $("#input3").keyup(function () {
        $("#target").text($(this.val()))
    });
    $("#input4").keydown(function () {
        $("#target").text($(this.val()))
    });
    $("#input5").keypress(function () {
        $("#target").text($(this.val()))
    });
});