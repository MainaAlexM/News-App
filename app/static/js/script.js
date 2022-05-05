var isTopics=false;
var isSources=true;
var isCountries=true;

$(document).ready(function(){
    $(".open-topics").click(function(){
        $(".topics").toggle();
        if (isTopics){
            isTopics=!isTopics
            $("#topics").removeClass();
            $("#topics").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isTopics=!isTopics
            $("#topics").removeClass();
            $("#topics").addClass("glyphicon glyphicon-menu-down");
        }
    })
    $(".open-sources").click(function(){
        $(".sources").toggle();
        if (isSources){
            isSources=!isSources
            $("#sources").removeClass();
            $("#sources").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isSources=!isSources
            $("#sources").removeClass();
            $("#sources").addClass("glyphicon glyphicon-menu-down");
        }
    })
    $(".open-countries").click(function(){
        $(".countries").toggle();
        if (isCountries){
            isCountries=!isCountries
            $("#countries").removeClass();
            $("#countries").addClass("glyphicon glyphicon-menu-up");
        }
        else{
            isCountries=!isCountries
            $("#countries").removeClass();
            $("#countries").addClass("glyphicon glyphicon-menu-down");
        }
    })
});