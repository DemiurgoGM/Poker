
const slider = document.getElementById("BettingRange");
const output = document.getElementById("BettingValue");
output.value = slider.value.toString();
slider.oninput = function() {
    output.value = this.value;
};
//
// {#function betpressed(e) {#}
// {#    window.alert("botao pressionado")#}

