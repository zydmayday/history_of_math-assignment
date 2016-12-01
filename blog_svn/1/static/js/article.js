$(function() {

	// 解决CSRF
	$(document).ajaxSend(function(event, xhr, settings) {  
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
        function sameOrigin(url) {  
            // url could be relative or scheme relative or absolute  
            var host = document.location.host; // host + port  
            var protocol = document.location.protocol;  
            var sr_origin = '//' + host;  
            var origin = protocol + sr_origin;  
            // Allow absolute or scheme relative URLs to same origin  
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||  
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||  
                // or any other URL that isn't scheme relative or absolute i.e relative.  
                !(/^(\/\/|http:|https:).*/.test(url));  
        }  
        function safeMethod(method) {  
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
        }  
      
        if (!safeMethod(settings.type) && sameOrigin(settings.url)) {  
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));  
        }  
    });  

	// 添加新的label
	$("#add-label-btn").on('click', function(e) {
		e.preventDefault();
		var currentObj = $(this),
			label_name = $('input#add-label').val();
		if (!label_name) {
			return false;
		};
		$.ajax({
			url: currentObj.data('url'),
			type: 'POST',
			dataType: 'json',
			data: {label_name: label_name},
		})
		.done(function(label) {
			if(label.created == true){
				$('div.labels').append($("<button class='btn btn-info label own' type='button' id='" + label.id + "'>" + label.name + "</button>"))
			} else {
				var currentObj = $(".form button.label#" + label.id);
				currentObj.toggleClass('own');
			}
			$('input#add-label').val('');
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
	});

	// 选择需要的标签
	$(".form").on('click', 'button.label', function(event, myName) {
		var currentObj = $(event.currentTarget);
		currentObj.toggleClass('own');
	});

	// 添加博文
	$('#add-article-btn').on('click', function(e) {
		e.preventDefault();
		var currentObj = $(this),
			own_labels = $('.labels button.own'),
			labels = [];
		own_labels.each(function(index, ele) {
			labels.push($(ele).attr('id'));
		});
		$.ajax({
			url: currentObj.data('url'),
			type: 'POST',
			dataType: 'html',
			data: {
				article_title: $('#article-title').val(),
				article_raw_content: $('#article-raw-content').val(),
				article_markdown_content: $('#article-markdown-content').val(),
				labels: labels
			},
		})
		.done(function() {
			window.location.replace('/')
			// $('#blog-main-content').html(new_form);
		})
		.fail(function(e) {
			console.log(e);
		})
		.always(function() {
			console.log("complete");
		});
		
	});

	// 添加时间线
	$('#add-timeline-btn').on('click', function(e) {
		e.preventDefault();
		var currentObj = $(this);
		$.ajax({
			url: currentObj.data('url'),
			type: 'POST',
			dataType: 'html',
			data: {
				timeline_date: $('#timeline-date').val(),
				timeline_tag: $('#timeline-tag').val(),
				timeline_description: $('#timeline-description').val()
			},
		})
		.done(function(new_form) {
			$('#blog-main-content').html(new_form);
		})
		.fail(function(e) {
			console.log(e);
		})
		.always(function() {
			console.log("complete");
		});
		
	});

	

	// 加载quicknote
	$(window).on('scroll', function(){
		if(typeof $('#loading').offset() == 'undefined') {
			return false;
		}
		var height = $(window).height();
		var scrollTop = $(window).scrollTop();
		var offsetTop = $('#loading').offset().top;
		var innerHeight = $('#loading').innerHeight();
		if(height+scrollTop>offsetTop+innerHeight){
			var url = $('#loading').data('url'),
				$loading = $('#loading').clone(true);
			$('#loading').remove();
			if(typeof url != 'undefined') {
				$('#loading').remove();
				$.ajax({
					url: url,
				})
				.done(function(data){
					$('#quicknote-list').append(data);
				})
				.fail(function(){
					alert('错误');
				});
			}
		}
	});

	// timeline popover
	// $('.timeline-tag').popover()

	// timeline的hidden tricks
	$('#hide-zyd-timeline').on('click', function(e) {
		$('#timeline-container.zyd .timeline-month-list').toggle();
	});


	// scroll-spy
	// $('body').scrollspy({ target: '.timeline-sidenav' })
	$('.timeline-sidenav').on('activate.bs.scrollspy', function (e) {
		console.log(e);
	})
});