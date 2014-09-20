 jQuery(function() {
      var form = jQuery("#postupdateform");
      form.submit(function(e) {
         var post_text = $( "#post_text" ).val();

        $.post('/theweber.in/post_status', $(this).serialize(), function(data){
            var obj = JSON.parse(data);
            console.log(obj)
            $("#userpostdiv").prepend("<div>"+obj.username+"</div><div><span>"+obj.post_title+"</span><span class='postdatestyles'>"+obj.publish_date+"</span></div><br/>===========================");

          });
        return false;
      });

    $(window).scroll(function(){
        if ($(window).scrollTop() == $(document).height() - $(window).height()){
            alert("scroll down");
            load_remain_user_posts();
        }
    });
});
function load_remain_user_posts(){
var ID=$(".message_box:last").attr("id");
alert(ID)
}