/* $(function(){
    $("input[name='submit']").click(function(){
        var $fileUpload = $('input[type="file"]')
        if(parseInt($fileUpload.get(0).files.length)>4){
            alert("tu a déjà dépassé a maximum de 4")
        }

    })


}) */ 


function checkPassword(){
    var password = $("#id_passwordN").val();
    var passwordC = $("#id_passwordC").val();

    

    if (password !== passwordC){
/*        alert("affiche confirmation "+passwordC +" password " +password) */
    $("#CheckPassword").html("mot de passe non identique")      
    $("#CheckPassword").css({"color":"red"})
}   
    else
{
    $("#CheckPassword").html("mot de passe identique")
    $("#CheckPassword").css({"color":"green"})}

}

$(document).ready(function(){
    $("#id_passwordC").keypress(checkPassword);
})




function fileValidation(){
    var profileInpDP = document.getElementById('file1');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }

}

function fileValidation_1(){
    var profileInpDP = document.getElementById('file2');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }

}

function fileValidation_2(){
    var profileInpDP = document.getElementById('file3');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }

}

function fileValidation_3(){
    var profileInpDP = document.getElementById('file3');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }

}





/* function fileValidation_1(){
    var profileInpDP = document.getElementById('file2');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }else{
        //Image preview
        if (profileInpDP.files && profileInpDP.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('displayProfile2').innerHTML = '<img src="'+e.target.result+'"/>';
            };
            reader.readAsDataURL(profileInpDP.files[0]);
        }
    }
}

function fileValidation_2(){
    var profileInpDP = document.getElementById('file3');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être :  .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }else{
        //Image preview
        if (profileInpDP.files && profileInpDP.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('displayProfile3').innerHTML = '<img src="'+e.target.result+'"/>';
            };
            reader.readAsDataURL(profileInpDP.files[0]);
        }
    }
}

function fileValidation_3(){
    var profileInpDP = document.getElementById('file4');
    var filePath = profileInpDP.value;
    var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if(!allowedExtensions.exec(filePath)){
        alert('Le fichier doit être : .jpeg/.jpg/.png/.gif seulement.');
        profileInpDP.value = '';
        return false;
    }else{
        //Image preview
        if (profileInpDP.files && profileInpDP.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById('displayProfile4').innerHTML = '<img src="'+e.target.result+'"/>';
            };
            reader.readAsDataURL(profileInpDP.files[0]);
        }
    }
}


/* function validate(file) {
    var ext = file.split(".");
    ext = ext[ext.length-1].toLowerCase();      
    var arrayExtensions = ["jpg" , "jpeg", "png", "bmp", "gif"];

    if (arrayExtensions.lastIndexOf(ext) == -1) {
        alert("Wrong extension type.");
        $("#image").val("");
    }
} */
