var walkOrCycle;
var distanceOrTime;
var disValue;

function go() {
    var calls = [ 'recommend/walking/distance', 'recommend/bicycling/time', 'recommend/walking/time', 'recommend/bicycling/distance'];


    if (walkOrCycle == 'walk'){
        if (distanceOrTime == 'distance') {
            gogo(calls[0] + '?distance=' + disValue);
        } else if (distanceOrTime == 'time'){
            gogo(calls[2] + '?duration=' + disValue);
        }
    }
    else if (walkOrCycle == 'cycle') {
        if (distanceOrTime == 'distance') {
            gogo(calls[3] + '?distance=' + disValue);
        } else if (distanceOrTime == 'time'){
            gogo(calls[1] + '?duration=' + disValue);
        }
    }
    return false;
}

function gogo(v){
    window.location.href = 'map.html?' + v;
}

function setWalk() {
    walkOrCycle = 'walk';
    $('#walk').addClass('active');
    $('#cycle').removeClass('active');
}

function setCycle() {
    walkOrCycle = 'cycle';
    $('#walk').removeClass('active');
    $('#cycle').addClass('active');
}

function setdisValue() {
    disValue = $('#disvalue').val();
}

function setDistance() {
    distanceOrTime = 'distance';
    $('#distance').addClass('active');
    $('#time').removeClass('active');
}

function setTime() {
    distanceOrTime = 'time';
    $('#distance').removeClass('active');
    $('#time').addClass('active');
}

function gogomap() {
    var url = window.location.search.substring(1);
    $.ajax({
        method: "GET",
        url: 'http://192.168.1.194:8080/' + url
    })
        .done(function( msg ) {
            map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: 56.012147, lng: -3.75928},
                zoom: 14
            });
            weather = msg.message;
            for (var i = 0; i < weather.length; i++) {
                alert(weather[i]);
            }
            loc = msg.nodes;
            for (var i = 0; i < loc.length; i++) {
                var marker = new google.maps.Marker({
                    position: { lat: parseFloat(loc[i].sight_pos.latitude), lng: parseFloat(loc[i].sight_pos.longitude) },
                    map: map
                });
                google.maps.event.addListener(marker, 'click', verify);
            }
        });
}

function verify() {
    var cod = prompt('Please enter the code');
    verifyCode(cod);
}

function verifyCode(code){
    $.ajax({
        method: "GET",
        url: 'http://192.168.1.194:8080/verify_code?code=' + code
    })
        .done(function( msg ) {
            if (msg == true) {
                alert('Congratulations');
            } else {
                alert('Wrong :(');
            }
        });
}

function initMap() {}