function delete_coffee_shop(){
    try{
        let form = document.getElementById('delete_form');
        form.addEventListener('submit', (event)=>{
            event.preventDefault();
            let ok = confirm('Are you sure? this action will delete the coffee shop');
            if(ok == true){
                form.submit();
            }

        })
    }catch{
        //pass
    }
}

function delete_comment(){

   try{
        let delete_comment_button = document.getElementById('delete-comment');
        let form = document.getElementById('delete-comment-form');
        delete_comment_button.addEventListener('click', ()=>{
            let ok = confirm('Are you sure?');
            if(ok == true){
                form.submit();
            }
        })

   }catch{
    //pass
   }

}

delete_coffee_shop();
delete_comment();