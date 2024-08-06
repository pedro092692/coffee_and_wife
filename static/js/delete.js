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

delete_coffee_shop();