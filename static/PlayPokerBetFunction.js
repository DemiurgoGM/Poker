// TODO
let money = document.URL.match(/money=([0-9]+)/)[1];
const betButton = document.getElementById("BettingSubmit");

betButton.onclick = function () {
    window.alert(document.getElementById("BettingRange").value);
};
