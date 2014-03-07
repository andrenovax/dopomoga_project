$(document).ready(function() {

    $('.readmore+p, .cancel').hide();

    /*===SUPPORT BUTTONS===*/
    $('.support').click(function(){
        var itemid;
        itemid = $(this).attr("data-itemid");
        $.get('/dopomoga/support_project/', {itemid: itemid}, function(){});
        $(this).prev().show();
        $(this).next().show();
        $(this).hide();
    });
    $('.resupport, .hsupport').click(function(){
        $(this).prev().show();
        $(this).next().show();
        $(this).hide();
    });
    $('.cancel').click(function(){
        $(this).next().show();
        $(this).next().next().hide();
        $(this).hide();
    });
});
