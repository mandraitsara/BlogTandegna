$(document).ready(function(){
    $("label[for='id_pack'],#id_pack,ul[class='errorlist']").hide()

    $("#id_type").change(function(){
        var id_type = $("#id_type").prop('selectedIndex')
        if(id_type == 0){
            $("label[for='id_pack'],#id_pack,ul[class='errorlist']").hide()            
        }else{
            $("label[for='id_pack'],#id_pack,ul[class='errorlist']").show()
        }
    })
    
    $("div.race").hide()

    //  $("input[name='race']").hide() // Cacher l'input avant categorie
    //  $(".race").hide()

    $('#category').change(function(){
        var test = $("#category").prop('selected', true)
        var nb = test.val()
        var id_category = $("div.race-"+nb)
        var category_id = $(".category_id-"+nb).val()
    
        let type = $(".type").val(category_id)

        let type_id = type.val()

        let input_category = $("#race-"+nb)
        let race_id = input_category.val(type_id)
        let id = race_id.val()

        if(type_id==id){
            $("div.race-"+id).show()
        }else{
            $("div.race").hide()
        }
        
        

        
      

    
        
       

    })
})

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  } 