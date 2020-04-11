// TODO
const betValue = document.getElementById("BettingRange").value;
let money = document.URL.match(/money=([0-9]+)/)[1];
const betButton = document.getElementById("BettingSubmit");

betButton.onclick = function () {
    window.alert(betValue);
};

// <script>
//             const playpokerfield = document.getElementById("MidFieldSet");
//             const betButton = document.getElementById("BettingSubmit");
//             betButton.onclick = function () {
//                 alert("Bet");
//                 playpokerfield.textContent += {{ deck.cards_list.pop }} + "\n";
//             }
//         </script>
