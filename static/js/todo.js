var table = $('#mytable').DataTable();

function table_onload(){
    table.clear()
    $.get({
        url: "getlist", async: false,
        success: function(data){
            if(data) {             
                table.rows.add( data['message'] ).draw();
            }
        }
    }) 
}


function save(){
    $.post({
        url: "addTodo",
        data: $('#todoform').serialize(),
        dataType: 'json',
        success: function(data){
            $('#add').modal('hide');
            table.clear()
            table.rows.add( data['message'] ).draw();   
        },
        error: function(xhr, status, error) {
            alert(error+". Please contact Administrator");
        }
    }) 
}

table_onload()