/*var jqxhr = $.ajax( "example.php" )
    .done(function() {
        alert( "success" );
    })
    .fail(function() {
        alert( "error" );
    })
    .always(function() {
        alert( "complete" );
    });*/

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
    window.location.href = v;
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