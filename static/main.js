$(document).ready(function() {
    
    //Tabs
    $('#tabs').tabs();
    $('#useZone').tabs();

    //hover states on the static widgets
    $('#dialog_link, ul#icons li').hover(
        function() { $(this).addClass('ui-state-hover'); }, 
        function() { $(this).removeClass('ui-state-hover'); }
    );
    //general option post 
    function option(name,value)
    {
        $.post("/option", {name:name, value:value});
    }
    
    
   //textarea changes
    $(".regex, #replace, #text").change(function(){
        
        $(".regex").change(function(){
            var value=$(this).val();
            $(".regex").val(value);
            });
        var name=$(this).attr("name");
        var value=$(this).val();
        $.post("/text", {name:name, value:value}, function(data){
            $("#result").html(data);
            });
        });
    
    //change the regex options
    $(".flag").click(function(){
        var name=$(this).attr("name");
        var checked=$(this).attr("checked");
        option(name, checked);
        $(".regex").change();
        });


        
    //tab changed; so, match:replace:split changed
    $( "#tabs" ).bind( "tabsshow", function(event, ui) {
        var sel= $( this ).tabs( "option", "selected" );
        option("action", sel);
        $(".regex").change();
    });
    
    //notify the CGI that the language has been changed 
    $("#langs").change(function(){
        var lang=$(this).val();
        option("lang", lang);
        $(".regex").change();
        });
});