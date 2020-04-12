
const slider = document.getElementById("BettingRange");
const numberBox = document.getElementById("BettingValue");
numberBox.value = slider.value.toString();
slider.oninput = function() {
    numberBox.value = this.value;
};

numberBox.oninput = function() {
    slider.value = this.value;
};
