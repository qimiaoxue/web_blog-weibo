var log = function() {
    console.log(arguments)
}


var todoTemplate = function(todo) {
    var t = todo
    var w = `
        <tr class="todo-table-cell">
            <td>${ t.id }</td>
            <td class="todo-table-content">${ t.task }</td>
            <td>${ t.created_time }</td>
            <td><button class="todo-table-delete" data-id="${ t.id }">delete</button></td>
            <td><button class="todo-table-update" data-id="${ t.id }">update</button></td>
        </tr>
    `
    return w
}


var bindEventTodoAdd = function() {
    $('#todo-add-button').on('click', function(){
        var button = $(this)
        var parent = button.parent()
        var task = parent.find('#todo-add-content').val()
        log('task', task)
        var form = {
            task: task,
        }
        var response = function(r) {
            log('success', arguments)
            log('r', r)
            if(r.success) {
                var t = r.data
                log('t', t)
                $('.todo-table-container').append(todoTemplate(t))
                alert('successfully add')
            } else {
                alert(r.message)
            }
        }
        api.todoAdd(form, response)
    })
}


var bindEventTodoDelete = function() {
    $('.todo-table-container').on('click', '.todo-table-delete', function(){
        var button = $(this)
        var todoId = button.data('id')
        log('todoId', todoId)
        var todoCell = button.closest('.todo-table-cell')
        log('todocell', todoCell)
        api.todoDelete(todoId, function(response){
            var r = response
            if(r.success) {
                log('success', arguments)
                $(todoCell).slideUp()
                alert('successfully delete')
            } else {
                log('error', arguments)
                alert("failed to delete")
            }
        })
    })
}


var bindEventTodoUpdate = function() {
    $('.todo-table-container').on('click', '.todo-table-update', function(){
        var button = $(this)
        var todoId = button.data('id')
        var todoCell = button.closest('.todo-table-cell')
        var todoContent =todoCell.find('.todo-table-content')
        var edit = `
            <div class="id-todo-edit">
                <input class="id-update-content">
                <button class="id-update-button">edit</button>
            </div>
        `
        $(todoCell).append(edit)
        $('.todo-table-container').on('click', '.id-update-button', function(){
            var div = $(this).parent()
            var todoUpdate = div.find('.id-update-content').val()
            var form = {
                task: todoUpdate, 
            }
            api.todoUpdate(todoId, form, function(response){
                var r = response
                log('r', r)
                if (r.success) {
                    var t = r.data
                    log('t', t)
                    $(todoContent).text(todoUpdate)
                    alert('successfully update')
                } else {
                    alert(r.message)
                }
            })
        })
    })
}


var bindEventTodoEditDelete = function() {
    $('.todo-table-container').on('click', '.id-update-button', function(){
        var button = $(this)
        var todoEdit = button.parent()
        $(todoEdit).remove()
    })
}


var bindEvents = function() {
    bindEventTodoAdd()
    bindEventTodoDelete()
    bindEventTodoUpdate()
    bindEventTodoEditDelete()
}


$(document).ready(function(){
    bindEvents()
})
