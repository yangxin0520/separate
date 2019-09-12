//保存图片验证码编号
var imageCodeId = "";


function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0,
            v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}


function generateImageCode() {
    //形成图片验证码的后端地址，设置到页面当中，让浏览请求验证码图片
    imageCodeId = generateUUID();
    var url = "/api/V1.0/image_codes/" + imageCodeId;
    $(".image-code img").attr("src", url);
}
$(document).ready(function () {
    generateImageCode();
})