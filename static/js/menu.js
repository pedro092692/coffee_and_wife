function show_menu(){
    let username = document.getElementById('username');
    username.addEventListener('click', ()=>{
        let menu = document.getElementById('menu');
          menu.classList.add('test')

        addEventListener('click', (event)=>{
            if(!event.composedPath().includes(menu) && !event.composedPath().includes(username)){
                menu.classList.remove('test');
            }
        })

    })

}

show_menu()