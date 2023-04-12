


$(document).ready(function(){
   
    

    $('input').keyup(function(){
        let textSaisi = $(this).val();
        if(textSaisi===""){
            if(!$(this).hasClass('is-invalid')){
                $(this).addClass('is-invalid');
            }
        }    
            else
            {
            $(this).removeClass('is-invalid');
            }
            
        })


        $('#id_type').on('click', function() {
            var value = $(this).val();
            var lbl = $('#lbl')
            // alert(value);

            /* if(value=='0' || value=='4')
            {
                $('#id_race').hide()
            }
            
            else{
                $('#id_race').show()
            }*/

            switch(value) {
                case 'Porc':
                    $('#lbl').hide()
                    $('#id_race').hide()
        
                  // code block
                  break;
                case 'Boeuf':
                    $('#lbl').show()
                    $('#id_race').show()
                    $('#id_race option[value="1"]').show()
                    $('#id_race option[value="2"]').show()
                    $('#id_race option[value="3"]').show()
                    $('#id_race option[value="4"]').hide()
                    $('#id_race option[value="5"]').hide()
                  break;
                
                case 'Provende':
                    $('#lbl').show()
                    $('#id_race').show()
                    $('#id_race option[value="1"]').hide()
                    $('#id_race option[value="2"]').hide()
                    $('#id_race option[value="3"]').hide()
                    $('#id_race option[value="4"]').show()
                     $('#id_race option[value="5"]').show()
                    break;
                default:
                    $('#id_race').hide()                    
                    $('#lbl').hide()
              } 

          });


          $('#regions').on('click', function() {            
            /*alert(idregions) */
          });
    
    });

