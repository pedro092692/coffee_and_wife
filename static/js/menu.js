function show_menu(){
    try{
        let username = document.getElementById('username');
        username.addEventListener('click', ()=>{
            let window_width = window.innerWidth;
            let menu = document.getElementById('menu');
            let mobile_menu = document.getElementById('mobile-menu');
            let nav = document.getElementById('nav');
            if(window_width > 500){
                menu.classList.add('test')

                close_menu(menu, window_width);
            }else{
                document.body.style.overflow = 'hidden';
                username.style.display = 'none';
                nav.style.display = 'none';
                mobile_menu.classList.add('mobile-show');
                let close = document.getElementById('close');
                close_menu(close, window_width, mobile_menu, nav);
            }
        })
    }catch{
        //pass
    }

}

function close_menu(button, window_width, mobile_menu){
    addEventListener('click', (event)=>{
         if(window_width > 500){
             if(!event.composedPath().includes(button) && !event.composedPath().includes(username)){
                    button.classList.remove('test');
             }
         }else{
            if(event.composedPath().includes(button)){
                nav.style.display = 'flex';
                username.style.display = 'block';
                document.body.style.overflow = 'auto';
                mobile_menu.classList.remove('mobile-show');
            }
         }
    })
}

show_menu()