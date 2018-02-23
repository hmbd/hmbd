/**
 * 表单验证模块(匿名模块)
 * Created by tsengdavid on 3/31/16.
 */

define(function () {
    /**
     * 邮箱验证
     * @param text
     * @returns {boolean}
     */
    function isEmail(text) {
        var regPattern = new RegExp();
        //编译之后会提高效率
        regPattern.compile("^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\\.([a-zA-Z0-9]+)$", "gi");
        if (regPattern.test(text)) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * 检查电话号码
     * @param text
     * @param isStrict 值未填写或者为false表示不严格检查（可以包含带减号的电话号码），但值为true时表示严格检查（标准的11位手机号）
     * @returns {boolean}
     */
    function isMobile(text, isStrict) {
        var pattern = new RegExp();
        if (typeof isStrict != "undefined" && isStrict == true) {
            pattern.compile("^1(\\d{10})$", "gi");
        } else {
            pattern.compile("^(\\d+)(\\-?)(\\d+)$", "gi");
        }
        if (pattern.test(text)) {
            return true;
        } else {
            return false;
        }

    }

    /**
     * 检查扩展名是否为图片
     * @param fullName
     * @returns {boolean}
     */
    function checkExtension(fullName, type) {
        if (typeof type == "undefined") {
            type = "image";
        }
        if (typeof fullName == "undefined" || fullName == null) {
            throw new Error("please input fullname");
            return false;
        }
        var pattern = new RegExp();
        // 获取扩展名
        var fileArr = fullName.split(".");
        var fileExt = fileArr[fileArr.length - 1];
        if (type == "video") {
            pattern.compile("^(mp4)|(avi)|(mov)|(rmvb)|(3gp)|(flv)|(webm)|(ogg)$", "gi");
        }
        else if (type == "image") {
            pattern.compile("^(jpg)|(png)|(jpeg)|(webp)|(gif)|(bmp)$", "gi");
        }
        else {
            throw new Error("类型只能为 image 或者 video");
        }
        if (pattern.test(fileExt)) {
            return true;
        }
        else {
            return false;
        }

    }

    /**
     * 判断是否为空
     * @param data
     * @returns {boolean}
     */
    function isNull(data) {
        if (typeof  data == "undefined") {
            return true;
        }
        return /^\s*$/gi.test(data)
    }

    var ret = new Object();
    ret.isEmail = isEmail;
    ret.isMobile = isMobile;
    ret.checkExtension = checkExtension;
    ret.isNull = isNull;
    return ret;
});