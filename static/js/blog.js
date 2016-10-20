var log = function() {
    console.log(arguments)
}


var blogCommentTemplate = function(comment) {
    var c = comment
    var t = `
        <div class="cell-inner item">
            <img class="avatar-s" src="${ c.avatar }" alt="">
            <span class="comment">${ c.comment }</span>
            <span class="time right span-margin">${ c.created_time }</span>
            <span class="name right span-margin">by:${ c.name }</span>
        </div>
    `
    return t
}


var bindEventCommentAdd = function() {
    $('.blog-comment-add').on('click', function(){
        var button = $(this)
        var parent = button.parent()
        var comment = parent.find('.blog-comment-content').val()
        log('comment', comment)
        var blog_id = parent.find('.comment-blog_id').val()
        log('blog_id', blog_id)
        var commentList = parent.parent().find('.comment-list')
        var form = {
            blog_id: blog_id,
            comment: comment,
        }
        var response = function(r) {
            log('success', arguments[0])
            log('r', r)
            if(r.success) {
                var name = r.name
                log('name', name)
                var c = r.data
                log('c', c)
                commentList.append(blogCommentTemplate(c))
                alert('successfully add')
            } else {
                alert(r.message)
            }
        }
        api.blogCommentAdd(form, response)
    })
}


var bindEvents = function() {
    bindEventCommentAdd()
}


$(document).ready(function(){
    bindEvents()
})
