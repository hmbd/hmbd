/**
 * Created by Administrator on 2016/8/27.
 */
define([ "notify"], function () {

        function dwnotify() {
            //遮罩显示
            var notify_html = '<span>没有库存啦</span>';
            $(".bottom-right").notify({
                message: {
                    html: notify_html
                },
                fadeOut: {delay: 2000}
            }).show();

        }

        var ret = new Object();
        ret.dwnotify = dwnotify;
        return ret
    }
);