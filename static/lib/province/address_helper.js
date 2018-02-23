/**
 * Created by lcx on 16-7-27.
 */
var requireArr = ["jquery", "city"];
define(requireArr, function ($) {
    var format = function (data) {
        var result = [];
        for (var i = 0; i < data.length; i++) {
            var d = data[i];
            if (d.name === "请选择") continue;
            result.push(d.name);
        }
        if (result.length) return result;
        return [""];
    };
    var sub = function (data) {
        if (!data.sub) return [""];
        return format(data.sub);
    };
    var raw = $.rawCitiesData;

    var getDistricts = function (p, c) {
        for (var i = 0; i < raw.length; i++) {
            if (raw[i].name === p) {
                for (var j = 0; j < raw[i].sub.length; j++) {
                    if (raw[i].sub[j].name === c) {
                        return sub(raw[i].sub[j]);
                    }
                }
            }
        }
        return [""];
    };

    function getProvinceCity() {
        $.getScript('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js', function () {
            if (remote_ip_info.ret == '1') {
                var pro_city_area = "";
                var province = remote_ip_info.province;
                var city = remote_ip_info.city;
                var area;
                area = getDistricts(province, city);
                pro_city_area += province + " " + city + " " + area[0];
                $("#city-picker").val(pro_city_area);
                $("#city-picker").cityPicker({
                    title: "选择收货地址"
                });
            }
        });
    }

    var ret = new Object();
    ret.getProvinceCity = getProvinceCity;
    return ret;
});