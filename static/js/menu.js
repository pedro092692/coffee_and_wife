function show_menu(){
    let username = document.getElementById('username');
    username.addEventListener('click', ()=>{
        let menu = document.getElementById('menu');
        menu.style.visibility = 'visible';
        menu.style.opacity = '1';

        addEventListener('click', (event)=>{
            if(!event.composedPath().includes(menu) && !event.composedPath().includes(username)){
                menu.style.visibility = 'hidden';
                menu.style.opacity = '0';
            }
        })

    })

}

show_menu()