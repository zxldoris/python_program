$(function () {
    //属性操作
    $("#attr_get").click(function () {
        alert($("#img_src img").attr("src"));
    });
    $("#attr_modify").click(function () {
        $("#img_src img").attr("src", "img/baidu.png");
    });
    $("#attr_remove").click(function () {
        $("#img_src img").removeAttr("src");
    });

    // 节点内容获取get html text val
    $("#node_html").click(function () {
        alert($("#get_html").html());
    });
    $("#node_text").click(function () {
        alert($("#get_text").text());
    });
    $("#node_val").click(function () {
        alert($("#get_val").val());
    });

    //设置
    //html包含标签
    $("#node_shtml").click(function () {
        $("#set_text").html("<strong>大叔，</strong>");
    });
    //自动过滤标签
    $("#node_stext").click(function () {
        $("#set_text").text("我们");
    });
    //表单里面属性
    $("#node_sval").click(function () {
        $("#set_html").val("不约");
    });

    //文档处理
    $("#dom_add").click(function () {
        $("#dom_opt ul").append("<li>在后面追加</li>");
    });
    $("#dom_pre_add").click(function () {
        $("#dom_opt ul").prepend("<li>在前面追加</li>");
    });
    $("#dom_to_add").click(function () {
        $("<li>在后面追加to</li>").appendTo("#dom_opt ul");
    });
    $("#dom_preto_add").click(function () {
        $("<li>在前面追加to</li>").prependTo("#dom_opt ul");
    });

    // insert before after
    $("#dom_after").click(function () {
        $("#dom_insert ul").after("<li>在后面追加</li>");
    });
    $("#dom_before").click(function () {
        $("#dom_insert ul").before("<li>在前面追加</li>");
    });
    $("#dom_insert_after").click(function () {
        $("<li>在后面追加insertAfter</li>").insertAfter("#dom_insert ul");
    });
    $("#dom_insert_before").click(function () {
        $("<li>在前面追加insertBefore</li>").insertBefore("#dom_insert ul");
    });

    // wrap unwrap
    $("#dom_wrap").click(function () {
        $("#wrap_unwrap p").wrap("<div style='color:red;'></div>");
    });
    $("#dom_unwrap").click(function () {
        $("#wrap_unwrap").unwrap("<div style='color:red;'></div>");
    });

    //文档处理
    $("#dom_empty").click(function () {
        $("#li_empty").empty();
    });
    $("#dom_remove").click(function () {
        $("#li_remove").remove();
    });
    $("#dom_clone").click(function () {
        alert($("#li_clone").clone().html());
    });

    //css class的操作
    $("#dom_addClass").click(function () {
        $("#dom_class").addClass("css_class");
    });
    $("#dom_removeClass").click(function () {
        $("#dom_class").removeClass("css_class");
    });
    $("#dom_toggleClass").click(function () {
        $("#dom_class").toggleClass("css_class");
    });

    // css 基础操作
    $("#dom_css").click(function () {
        $("#dom_set").css({border:"1px solid red",height:"20px",width:"100px"});
    });
    $("#dom_height").click(function () {
        $("#dom_set").height("100px");
        $("#dom_set").width("100px");
    });
});