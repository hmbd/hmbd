requirejs.config({
    urlArgs: CONFIG.version,
    baseUrl: CONFIG.baseUrl + "/province",
    paths: {
        "jquery": "../../js/jquery-1.12.3.min",
        "notify": "../../bootstrap/js/bootstrap-notify",
        "js.cookie": "../../js/js.cookie",
        "jquery.weui": "../../city-picker/js/jquery-weui",
        "city": "../../city-picker/js/city-picker",
        "jquery.bootstrap": "../../bootstrap/js/bootstrap.min",
        "qrcode": "../../js/jquery.qrcode",
        "bootbox": "../../bootstrap/plugin/bootbox.min",
        "validate": "../validation/form"
    },
    shim: {
        "notify": {
            "deps": ["jquery.bootstrap"]
        },
        "qrcode": {
            "deps": ["jquery"]
        },
        "jquery.bootstrap": {
            "deps": ["jquery"]
        },
        "jquery.weui": {
            "deps": ["jquery"]
        },
        "city": {
            "deps": ["jquery"]
        }
    }
});
var arr = ["jquery", "my_notify", "js.cookie", "address_helper", "jquery.weui", "city", "qrcode", "jquery.bootstrap", "bootbox", "validate"];
require(arr, function ($, my_notify, cookie) {
    var pMessage_top = $(window).height();
    $(".pMessage").css("margin-top", (pMessage_top * 1.0 / 2));
    var code_button = cookie.get("code_button");
    if(code_button== "code"){
        $(".qr_close").show();
        $(".app_alipay").hide();
    }
    else if(code_button== "button"){
        $(".qr_close").hide();
        $(".app_alipay").show();
    }
    else{
        $(".qr_close").show();
        $(".app_alipay").hide();
    }
    // 填写过信息直接填充
    var now_tel = $("#telephone").val();
    if (!now_tel && cookie.get("telephone")) {
        $("#telephone").val(cookie.get("telephone"));
    }
    if(province_city){
        $("#city-picker").val(province_city);
        $("#city-picker").cityPicker({
            title: "选择收货地址"
        });
    }
    else {
        if (!cookie.get("province")) {
            var address_helper = require("address_helper");
            address_helper.getProvinceCity();
        }
        else{
            $("#city-picker").val(cookie.get("province"));
            $("#city-picker").cityPicker({
                title: "选择收货地址"
            });
        }
    }
    var now_address = $("#address").val();
    if (!now_address && cookie.get("address")) {
        $("#address").val(cookie.get("address"));
    }
    // 监听光标
    $('#city-picker').bind('click', function () {
        $("#city-picker").focus();
    });
    // 返回按钮
    $('#btnBack').click(function () {
        //var bootbox = require("bootbox");
        //bootbox.confirm(("确定取消付款?"), function(result){
        //    if(result) {
        //        //window.location.href = document.referrer;//返回到上一个页面
        //        window.history.go(-1);
        //    }
        //});
        window.history.go(-1);
    });
    // 精确乘法结果
    function accMul(arg1,arg2){
        var m=0,s1=arg1.toString(),s2=arg2.toString();
        try{m+=s1.split(".")[1].length}catch(e){}
        try{m+=s2.split(".")[1].length}catch(e){}
        return Number(s1.replace(".",""))*Number(s2.replace(".",""))/Math.pow(10,m)
    }
    $('#spanPlus').click(function () {
        var amount = parseInt($('#spanCurrentNum').val());
        if(amount < max_amount) {
            var now_amount = amount + 1;
            $('#spanCurrentNum').val(now_amount);
            var commodity_price = parseFloat($('#commodity_price').text());
            var result = accMul(commodity_price, now_amount);
            $('#sum_price').html(result);
        }
        else{
            my_notify.dwnotify();
        }
    });


    $('#spanMinus').click(function () {
        var amount = parseInt($('#spanCurrentNum').val());
        if (amount > 1) {
            var now_amount = amount - 1;
            $('#spanCurrentNum').val(now_amount);
            var commodity_price = parseFloat($('#commodity_price').text());
            var result = accMul(commodity_price, now_amount);
            $('#sum_price').html(result);
        }
    });
    // 立即付款
    $('#buy-now-qrcode').bind('click', function () {
        var bootbox = require("bootbox");
        var validate = require("validate");
        // 手机号码
        var tel = $.trim($("#telephone").val());
        // 地区
        var province = $("#city-picker").val();
        // 详细地址
        var address = $.trim($("#address").val());
        // 购买数量
        var now_amount = $('#spanCurrentNum').val();
        // 总价
        var price_sum = $('#sum_price').text();
        if (!validate.isMobile(tel, true)) {
            bootbox.alert("请输入正确的号码");
            return false;
        }
        if (province == "--请选择--" || validate.isNull(province)) {
            bootbox.alert("未选择收货地址");
            return false;
        }

        if (validate.isNull(address)) {
            bootbox.alert("详细地址不能为空");
            return false;
        }
        // 手机号码、省市区、详细地址存入cookie
        cookie.set("telephone", tel, {expires: 365});
        cookie.set("province", province, {expires: 365});
        cookie.set("address", address, {expires: 365});
        $.ajax({
            url: location.href,
            type: "POST",
            data: {
                "telephone": tel,
                "address": province + '|' + address,
                "device_id": 1,
                "now_amount": now_amount,
                "price_sum": price_sum
            },
            dataType: "json",
            success: function (res) {
                if (res.code == 0) {
                    var protocol = location.protocol;
                    var host = location.host;
                    var commodity_url = "https://hmbd.github.io/";
                    $("#qrCode").html("");
                    $("#qrCode").qrcode({
                        render: "canvas", //设置渲染方式 （有两种方式 table和canvas，默认是canvas）
                        width: 260, //宽度
                        height: 260, //高度
                        //typeNumber: -1, //计算模式
                        //correctLevel: 0, //纠错等级
                        text: utf16to8(commodity_url), //任意内容
                        src: logo_path // canvas模式才会显示logo,大小为宽高的2.5比例，logo_height = 200/2.5
                    });
                    var margin_top = $(window).height() - $("#codeMessage").height();
                    var margin_left = $(window).width() - $("#codeMessage").width();
                    var alipay_left = $(window).width() - $("#buy-alipay").width();
                    var alipay_top = ($(window).height() + $("#buy-alipay").height() + $(".imgAlipay").height()) * 1.0 / 2;
                    var buy_top = $(window).height() - $("#buy-alipay").height() + $(".imgAlipay").height();
                    $("#buy-alipay").css("top", (buy_top * 1.0 / 2) - 15);
                    $("#buy-alipay").css("left", (alipay_left * 1.0 / 2));
                    $(".alipayMessage1").css("top", alipay_top + 15);
                    $(".alipayMessage2").css("top", alipay_top + 38);
                    $(".login-top").css("top", (margin_top * 1.0 / 2));
                    $(".login-top").css("right", (margin_left * 1.0 / 2));
                    $(".pay_change").css("top", (margin_top * 1.0 / 2));
                    $(".pay_change").css("right", (margin_left * 1.0 / 2));
                    $("#codeMessage").css("margin-top", (margin_top * 1.0 / 2));
                    $(".masking").show();
                    $(".div-qrcode").show();
                    var js_order = cookie.get("Order_Produce_" + res.data);
                    if(!js_order){
                        cookie.set("Order_Produce_" + res.data, res.data, {expires: 365});
                    }
                }
                else {
                    bootbox.alert(res.msg);
                }
            },
            error: function () {
                bootbox.alert("保存信息失败");
            }
        });
    });
    // 按钮切换二维码
    $('#qrcode-trigger').bind('click', function () {
        var margin_top = $(window).height() - $("#codeMessage").height();
        var margin_left = $(window).width() - $("#codeMessage").width();
        $(".code_close").css("top", (margin_top * 1.0 / 2));
        $(".code_close").css("right", (margin_left * 1.0 / 2));
        $(".qr_close").show();
        $(".app_alipay").hide();
    });
    // 二维码切换按钮
    $('.pay_change').bind('click', function () {
        $(".qr_close").hide();
        $(".app_alipay").show();
    });
    // 点击二维码关闭付款
    $('.codeImg').bind('click', function () {
        $(".masking").hide();
        $(".div-qrcode").hide();
    });
    // 点击支付宝图片关闭付款
    $('.imgAlipay').bind('click', function () {
        $(".masking").hide();
        $(".div-qrcode").hide();
    });
});