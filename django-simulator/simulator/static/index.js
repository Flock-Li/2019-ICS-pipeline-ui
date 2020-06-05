
$(function(){
    $("body").delegate(".comment","propertychange input",function(){
        if($(this).val().length>0){
            $(".send").prop("disabled",false);
        }else{
            $(".send").prop("disabled",true);
        }
    });
    // fresh();
    $(".send").click(function(){
        var $text = $(".comment").val();
        var post_data={
            "id":$text,
            "time": getDate(),
            "acc":0,
            "ref":0,
        };
        console.log(post_data);
        console.log(typeof post_data);
        $.ajax({
            type:"POST",
            url:"/postcomment/",
            data:post_data,
            headers: {
                "X-CSRFToken": getCookie("csrftoken") 
            },
            success:function(xhr){
                console.log("success");
            },
            error:function(xhr){
                console.log("error");
            },
        });
        var $weibo = createEle1($text);
        $(".messagelist").prepend($weibo);
        $(".comment").val("");

    });
    fresh();
    function fresh(){
        var formData = new FormData($("#insertForm")[0]);
        $.ajax({
            type:"GET",
            url:"/comment/",
            data:formData,
            contentType: false,
            processData: false ,
            success:function(xhr){
                console.log("success");
                data = JSON.parse(xhr);
                for(var key in data){
                    var item = data[key];
                    var $weibo = createEle(item);
                    $(".messagelist").prepend($weibo);
                }

            },
            error:function(xhr){
                console.log("error");
            },
        });
    }
    function update(content,flag){
        var pre_data={
            "con":content,
            "fla":flag,
        };
        console.log(pre_data)
        console.log(typeof pre_data);
        $.ajax({
            type:"POST",
            url:"/add/",
            data:pre_data,
            headers: {
                "X-CSRFToken": getCookie("csrftoken") 
            },
            success:function(xhr){
                console.log("success")
            },
            error:function(xhr){
                console.log("error");
            },
        });
    }
    function createEle(obj){
        var $weibo = $("<div class=\"infocom\">\n" +
        "            <p class=\"infoText\">"+obj.id+"</p>\n" +
        "            <p class=\"infoOperation\">\n" +
        "                <span class=\"infoTime\">"+formartDate(obj.time)+"</span>\n" +
        "                <span class=\"infoHandle\">\n" +
        "                    <i class=\"iconfont\ Top\" >&#xe680</i><a href=\"javascript:;\" class='infoTop'>"+obj.acc+"</a>\n" +
        "                    <i class=\"iconfont\ Down\">&#xe6cb</i><a href=\"javascript:;\" class='infoDown'>"+obj.ref+"</a>\n" +
        "                    <i class=\"iconfont\ Del\">&#xe615</i><a href=\"javascript:;\" class='infoDel'>delete</a>\n" +
        "                </span>\n" +
        "            </p>\n" +
        "        </div>");
        return $weibo;
    }
    function createEle1(text){
        var $weibo = $("<div class=\"infocom\">\n" +
        "            <p class=\"infoText\">"+text+"</p>\n" +
        "            <p class=\"infoOperation\">\n" +
        "                <span class=\"infoTime\">"+getDate()+"</span>\n" +
        "                <span class=\"infoHandle\">\n" +
        "                    <i class=\"iconfont\ Top\" >&#xe680</i><a href=\"javascript:;\" class='infoTop'>"+0+"</a>\n" +
        "                    <i class=\"iconfont\ Down\">&#xe6cb</i><a href=\"javascript:;\" class='infoDown'>"+0+"</a>\n" +
        "                    <i class=\"iconfont\ Del\">&#xe615</i><a href=\"javascript:;\" class='infoDel'>delete</a>\n" +
        "                </span>\n" +
        "            </p>\n" +
        "        </div>");
        return $weibo;
    }
    function formartDate(time){
        var date = new Date(time);
        var arr = [date.getFullYear() + "-",
                    date.getMonth() + 1 + "-",
                    date.getDate() + " ",
                    date.getHours() + ":",
                    date.getMinutes() + ":",
                    date.getSeconds()];       
        return arr.join("");
    }
    function getDate(){
        var date = new Date();
        var arr = [date.getFullYear() + "-",
                    date.getMonth() + 1 + "-",
                    date.getDate() + " ",
                    date.getHours() + ":",
                    date.getMinutes() + ":",
                    date.getSeconds()];       
        return arr.join("");
    }
    // 正则匹配cookie中的csrftoken，传入cookie名字
    function getCookie(name) {
        var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return r ? r[1] : undefined;
    }
    $("body").delegate(".infoTop", "click", function () {
        var a=$(this).parents(".infocom");
        var b=a.children(".infoText");
        var content = b.html();
        update(content,"1");
        $(this).text(parseInt($(this).text()) + 1);
    });
    $("body").delegate(".infoDown", "click", function () {
        var a=$(this).parents(".infocom");
        var b=a.children(".infoText");
        console.log(b.html());
        update(b.html(),"0");
        $(this).text(parseInt($(this).text()) + 1);
    });
    $("body").delegate(".infoDel", "click", function () {
        $(this).parents(".infocom").remove();
    });
});
