


function incrementVal(selector){
    var $item = selector;
    var $curVal = $item.attr("value");
    $item.attr("value", parseInt($curVal) +1);
}

$("#increment").on("click",function(){
    incrementVal($('#counter'))
})