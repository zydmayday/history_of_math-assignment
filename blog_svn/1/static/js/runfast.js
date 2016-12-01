$(function() {

	// 解决CSRF
    function solveCSRF(){
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
    }

    solveCSRF();
	

    function getNewestPage(){
        playerName = $('#playerInfo').attr('playerName')
        // console.log(playerName)
        $.ajax({
            url: "/runfast/game",
            type: 'post',
            dataType: 'html',
            data: {playerName: playerName}
        })
        .done(function( html ) {
            $('#runfast').html(html);
            if ($('#playerInfo').attr('gameover') == 'True'){
                alert('游戏结束！谢谢')
            }else{
                myTurn = $('#playerInfo').attr('myTurn')
                if (myTurn == 'True'){
                    alert('你的回合！');
                }else{
                    setTimeout(getNewestPage, 1000);
                }
            }
            // solveCSRF();
        })
        .fail(function() {
            console.log("error");
        })
    }
    
    $('#join').on('click', function(e){
        e.preventDefault();
        playerName = $('#playerName').val();
        url = $('#join').attr('url')
        // console.log(selectedCards);
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'html',
            data: {playerName: playerName},
        })
        .done(function(html) {
            setTimeout(getNewestPage, 1000);
			$('#runfast').html(html);
			// solveCSRF();
		})
		.fail(function() {
			console.log("error");
		})
		
	});

    $( "#runfast" ).on( "click", "#owncards .card", function() {
        if ($(this).attr('isSelected') == 'true'){
            $(this).attr('isSelected', 'false')
        }else{
            $(this).attr('isSelected', 'true')
        }
            
    });

    $( "#runfast" ).on( "click", "#playCard", function(e) {
        e.preventDefault();
        playerName = $('#playerInfo').attr('playerName')
        cards = [];
        $("#owncards .card[isSelected='true']").each(function(){
            cards.push($(this).attr('name'));
        });
        url = $('#playCard').attr('url');
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'html',
            data: {
                'cards': cards,
                playerName: playerName
            },
        })
        .done(function(html) {
            $('#runfast').html(html);
            if ($('#playerInfo').attr('gameover') == 'True') {
                alert('你胜出了！');
            }else{
                isLegal = $('#playerInfo').attr('isLegal');
                if (isLegal == 'True'){
                    setTimeout(getNewestPage, 1000);
                }else{
                    alert('出牌不合法！重新出牌');
                }
            }
            // solveCSRF();
        })
        .fail(function() {
            console.log("error");
        })
    });

    $('#runfast').on('click', '#pass', function(e) {
        e.preventDefault();
        playerName = $('#playerInfo').attr('playerName')
        url = $(this).attr('url')
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'html',
            data: {
                playerName: playerName
            },
        })
        .done(function(html) {
            $('#runfast').html(html);
            myTurn = $('#playerInfo').attr('myTurn');
            if (myTurn == 'True'){
                alert('你的回合，请走牌！');
            }else{
                setTimeout(getNewestPage, 1000);
            }
            // solveCSRF();
        })
        .fail(function() {
            console.log("error");
        })
    });

    $('#runfast').on('click', '#reset', function(e) {
        e.preventDefault();
        url = $(this).attr('url')
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'json',
            data: {
                msg: 'i want to reset'
            }
        })
        .done(function(msg) {
            alert(msg);
        })
        .fail(function() {
            console.log("error");
        })
    });

	
});
