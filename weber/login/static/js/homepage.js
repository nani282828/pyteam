 jQuery(function() {
      var form = jQuery("#postupdateform");
      form.submit(function(e) {
         var post_text = $( "#post_text" ).val();
         alert(post_text);
        $.post('/theweber.in/post_status', $(this).serialize(), function(data){
            var obj = JSON.parse(data);
            console.log(obj)
          });
        return false;
      });
  });