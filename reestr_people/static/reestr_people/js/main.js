function changeClass(){
    $(this).prev().toggleClass('active')
    }
    $(function(){
        $('div h4').click(function(){
            $(this).next().slideToggle();
            $(this).toggleClass('active');
        })
    })