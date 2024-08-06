function show_review_form(){
    let leave_comment_button = document.getElementById('leave-comment');
    let review_form = document.getElementById('review-form');
    try{
        active_user = leave_comment_button.getAttribute('active_user');
            leave_comment_button.addEventListener('click', function(){
            show_form(review_form, leave_comment_button, active_user)
        });
    }catch{
        //pass
    }


    try{
        let edit_comment = document.getElementById('edit-comment');
        let comment = edit_comment.parentElement.previousElementSibling.textContent;
        edit_comment.addEventListener('click', ()=>{
           review_form.style.display = 'flex';
           review_form.comment.value = comment.trim();
        });
    }catch{
        // pass
    }


}

function show_form(review_form, button, active_user, hide_button=true){
    if(active_user == 'True'){
        review_form.style.display = 'flex';
        if(hide_button){
            button.style.display = 'none';
        }
    }else{
        window.location.href = '/login?next=' + window.location.href +'#reviews';
    }
}

show_review_form();