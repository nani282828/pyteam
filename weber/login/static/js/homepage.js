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
            //alert("scroll down");
            load_remain_user_posts();
        }
    });
});
function load_remain_user_posts(){
var post_id=$(".message_box:last").attr("id");
//alert(post_id)
var csrftoken = getCookie('csrftoken');

 /*$.post('/theweber.in/load_more_posts',{'last_msg_id':post_id,'csrfmiddlewaretoken':csrftoken},function(data){
            var obj = JSON.parse(data);
            console.log(obj)
            //$("#userpostdiv").prepend("<div>"+obj.username+"</div><div><span>"+obj.post_title+"</span><span class='postdatestyles'>"+obj.publish_date+"</span></div><br/>===========================");

          });*/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}



$.ajax({
		type: 'post',
		url: '/theweber.in/load_more_posts',
		data: {'last_msg_id':post_id,'csrfmiddlewaretoken':csrftoken},
		dataType: "json",
		beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
             }
         },
		complete: function(data){
		    var obj = JSON.parse(data);
			alert(obj.post_title)
			console.log(obj)

		}
	});

}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}