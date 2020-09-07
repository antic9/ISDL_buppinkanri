$("#btn btn-primary btn-block btn-flat").click(function(event){
         event.preventDefault();

     $('form').fadeOut(500);
     $('.wrapper').addClass('form-success');
});