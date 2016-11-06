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

var map;

function gogomap() {
    var url = window.location.search.substring(1);
    $.ajax({
        method: "GET",
        url: 'http://192.168.1.194:8080/' + url,
    })
        .done(function( msg ) {
            message = msg.message;
            for ( x in message) {
                alert(x);
            }
            location = msg.nodes
            for (l in location) {
                new google.maps.Marker({
                    position: location.sight_pos,
                    map: map
                });
            }
        });

}

function verifyCode(code){
    $.ajax({
        method: "GET",
        url: 'http://192.168.1.194:8080/verify_code?code=' + code,
    })
        .done(function( msg ) {
            return JSON.parse(msg);
        });
}

