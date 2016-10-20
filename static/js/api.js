var api = {}


api.ajax = function(url, method, form, callback) {
    var data = JSON.stringify(form)
    var request = {
        url: url,
        type: method,
        contentType: 'application/json',
        data: data,
        success: function(response) {
            var r = JSON.parse(response)
            callback(r)
        },
        error: function(err) {
            var r = {
                'success': false,
                message: 'network error'
            }
            callback(r)
        }
    }
    $.ajax(request)
}


api.post = function(url, form, response) {
    api.ajax(url, 'post', form, response)
}


api.get = function(url, response) {
    api.ajax(url, 'get', {}, response)
}


api.todoAdd = function(form, response) {
    var url = '/api/todo/add' 
    api.post(url, form, response)
}


api.todoDelete = function(todoId, response) {
    var url = '/api/todo/delete/' + todoId
    api.get(url, response)
}


api.todoUpdate = function(todoId, form, response) {
    var url = '/api/todo/update/' + todoId
    api.post(url, form, response)
}


api.blogCommentAdd = function(form, response) {
    var url = '/api/blog/comment/add'
    api.post(url, form, response)
}


api.weiboAdd = function(form, response) {
    var url = '/api/weibo/add' 
    api.post(url, form, response)
}


api.weiboDelete = function(weiboId, response) {
    var url = '/api/weibo/delete/' + weiboId
    api.get(url, response)
}
