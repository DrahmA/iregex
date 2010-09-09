$(document).ready(function() { 
    function option(name,value)
    {
        $.post("/option", {name:name, value:value}, function(data){
            //alert(data);
            });
    }
    $(".flag").click(function(){
        option($(this).attr("name"),$(this).attr("checked"));
        });

    //Tabs
    $('#tabs').tabs();
    $('#useZone').tabs();

    //hover states on the static widgets
    $('#dialog_link, ul#icons li').hover(
        function() { $(this).addClass('ui-state-hover'); }, 
        function() { $(this).removeClass('ui-state-hover'); }
    );

}); 
