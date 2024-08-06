function show_review_form(){
    let leave_comment_button = document.getElementById('leave-comment');
    let review_form = document.getElementById('review-form');
    active_user = leave_comment_button.getAttribute('active_user');
    leave_comment_button.addEventListener('click', ()=>{
        if(active_user == 'True'){
            review_form.style.display = 'flex';
            leave_comment_button.style.display = 'none';
        }else{
            window.location.href = '/login?next=' + window.location.href +'#reviews';
        }

    })


}

show_review_form();