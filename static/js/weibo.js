var log = function() {
    console.log(arguments)
}


var weiboTemplate = function(weibo) {
    var w = weibo
    var t = `
        <div class="weibo-cell cell item">
            <img src="${ w.avatar }" class="avatar">
            <span>${ w.weibo }</span>
            <span class="right span-margin">${ w.created_time }</span>
            <span class="right span-margin">by: ${ w.name }</span>
            <div class="right span-margin">
                <button class="weibo-delete" data-id="${ w.id }">delete</button>
                <a href="#" class="com">comment(${ w.comments_num })</a>
            </div>
            <div class="comment-div hide">
                <div class="">
                </div>
                <input type="hidden" name="weibo_id" value="${ w.id }">
                <input name="comment" class="left m" placeholder="Comment">
                    <button>publish comment</button>
            </div>
        </div>
    `
    return t
}


var bindEventCommentToggle = function() {
    $('a.com').on('click', function(){
        $(this).parent().next().slideToggle()
        return false;
    })
}


var bindEventWeiboAdd = function() {
    $('#id-button-weibo-add').on('click', function(){
        var weibo = $('#id-input-weibo').val()
        log('weibo,', weibo)
        var form = {
            weibo: weibo,
        }

        var response = function(r) {
            log('success', arguments)
            log(r)
            if(r.success) {
                var w = r.data
                $('.weibo-container').prepend(weiboTemplate(w))
                alert("success add weibo")
            } else {
                alert(r.message)
            }
        }
        api.weiboAdd(form, response)
    })
}


var bindEventWeiboDelete = function() {
    $('.weibo-container').on('click', '.weibo-delete', function(){
        var button = $(this)
        var weiboId = button.data('id')
        log("weiboId", weiboId)
        var parent = button.parent()
        // var weiboCell =parent.parent().find('.weibo-cell cell item') WRONG
        // var weiboCell =parent.parent()
        var weiboCell = $(this).closest('.weibo-cell') 
        log('weibocell', weiboCell)
        api.weiboDelete(weiboId, function(response) {
            var r = response
            if(r.success) {
                log('success', arguments)
                $(weiboCell).slideUp()
                log('delete success')
                alert("success delete")
            } else {
                log('error', arguments)
                alert("delete false")
            }
        })
    })
}


var bindEvents = function() {
    bindEventCommentToggle()
    bindEventWeiboAdd()
    bindEventWeiboDelete()
}


$(document).ready(function(){
    bindEvents()
})
