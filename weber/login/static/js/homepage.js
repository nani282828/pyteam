 jQuery(function() {
      var form = jQuery("#postupdateform");
      form.submit(function(e) {
         var post_text = $( "#post_text" ).val();

        $.post('/theweber.in/post_status', $(this).serialize(), function(data){
<<<<<<< HEAD
            //var obj = JSON.parse(data);
            console.log(data);
            $("#userpostdiv").prepend(data);
=======
            var obj = JSON.parse(data);
            console.log(obj)
            $("#userpostdiv").prepend("<div>"+obj.username+"</div><div class='message_box' id='"+obj.id+"'><span>"+obj.post_title+"</span><span class='postdatestyles'>"+obj.publish_date+"</span></div><br/>===========================");
>>>>>>> 3bcb87ffc783c7ed7ea7c54aee8890dcc91e889c
            $("#post_text").val('');
          });
        return false;
      });
//=========search method==============
$('#search').keyup(function() {
         $.ajax({
            type: "POST",
            url: "/theweber.in/search",
            data: {
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });

    });
<<<<<<< HEAD
    //========================update info================
     jQuery("#updateinfo").submit(function( event ) {

        $.post('/theweber.in/updateinfo', $(this).serialize(), function(data){
            console.log(data)
            $("#updatestatus").html(data);
          });
        return false;
      });

//================send friend request====================
        jQuery("#sendrequest").submit(function( event ) {
        $.post('/theweber.in/sendrequest', $(this).serialize(), function(data){
            console.log(data)
            alert(data)
            //$("#updatestatus").html(data);
          });
        return false;
      });

});
=======

});


>>>>>>> 3bcb87ffc783c7ed7ea7c54aee8890dcc91e889c
  $(window).scroll(function(){
        if ($(window).scrollTop() == $(document).height() - $(window).height()){
            //alert("scroll down");

            load_remain_user_posts();
        }
    });

function searchSuccess(data, textStatus, jqXHR){
    $('#search-results').html(data);
         console.log(data);
}


function load_remain_user_posts(){
    var post_id=$(".message_box:last").attr("id");
    var csrftoken = getCookie('csrftoken');
    //alert(post_id)

    $.post('/theweber.in/load_more_posts',{'post_id':post_id,'csrfmiddlewaretoken':csrftoken}, function(data){

    if (data != "") {
        $(".message_box:last").after(data);
    }
    else
         console.log("NO DATA FOUDN")
    //$('div#last_msg_loader').empty();
    //$("#userpostdiv").append(data)

    });
 }

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
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



function profile(username){
     alert(username)
     $.ajax({
            type: "POST",
            url: "/show_profile",
            data: {
                'to_user':username,
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: request_sent_not,
            dataType: 'html'
        });
}

function request_sent_not(data, textStatus, jqXHR)
{
    alert(data)
    console(log.data)
}


<<<<<<< HEAD
=======
$(function(){



});

>>>>>>> 3bcb87ffc783c7ed7ea7c54aee8890dcc91e889c
