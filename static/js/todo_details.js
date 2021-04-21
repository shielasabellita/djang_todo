$("#is_done").on('change', function(){
    $(this).val(this.checked ? 1 : 0);
})

function set_isdone_val(){
    let isdone = $('#is_done')
    isdone.prop('checked', isdone.val()==1 ? true : false);
}


function save(){
    $.post({
        url: "edit",
        data: $('#editform').serialize(),
        dataType: 'json',
        success: function(data){
            alert("Successfully Updated");
        },
        error: function(xhr, status, error) {
            alert(error+". Please contact Administrator");
        }
    })
}

function del(id){
    console.log("clicked deleted", id)
    if (confirm("Are you sure you want to delete?")){
        $.get({
            url: "delete?id="+id,
            success: function(data){
                window.location.replace("dashboard")
            },
            error: function(xhr, status, error) {
                alert(error+". Please contact Administrator");
            }
        }) 
    }
    
}

set_isdone_val()