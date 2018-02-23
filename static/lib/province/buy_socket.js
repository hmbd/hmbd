/**
 * Created by lcx on 16-7-27.
 */
var requireArr = ["jquery", "bootbox"];
define(requireArr, function ($, bootbox) {
    function init(order_id) {
        var host = '11';
        // 消息计数
        var msgCount = 0;
        // 授权票据
        var ticket = "1";
        // 创建一个Socket实例
        var socket = new WebSocket(host);


        function showMsg(msg) {
            $("#display").append("<p style='color: red;'>" + msg + "</p>");
        }

        // 打开Socket
        socket.onopen = function (event) {
            console.log("<span style='color:green;'>连接成功,websocket服务器地址为：" + host + "</span>");
            // 发送一个注册消息，订阅mac地址为“C89346423654”的设备
            var reg = '{"k":"register","v":{"session_id":"'+order_id+'"},"ticket":"' + ticket + '"}';
            console.log('提交注册信息：' + reg);
            socket.send(reg);
            msgCount++;
            // 监听消息
            socket.onmessage = function (event) {
                console.log("监听消息");
                console.log(event.data);
                var res = JSON.parse(event.data);
                if (res.code == 0 && msgCount == 1) {
                    var msg = '{"k":"subscribe","v":["'+order_id+'"],"ticket":"' + ticket + '"}';
                    console.log('订阅主题：' + msg);
                    socket.send(msg);
                    msgCount++;
                }
                console.log(res);
                if (res.data) {
                    if (res.data[0].data.trade_status == 'TRADE_SUCCESS') {
                        bootbox.alert("付款成功");
                        //window.location.href = document.referrer;//返回到上一个页面
                        window.history.go(-1);
                    }
                    else {
                        showMsg("付款失败");
                    }
                }
            };

            // 监听Socket的关闭
            socket.onclose = function (event) {
                console.log('Client notified socket has closed', event);
            };

//        socket.onmessage = function (event) {
//            showMsg(event.data);
//        };

            // 关闭Socket....
            //socket.close()
        };

        socket.onerror = function (event) {
            console.log("连接失败了：" + event);
        }

    }

    var ret = new Object();
    ret.init = init;
    return ret;
});