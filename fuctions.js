function showTransferForm(){

    var submission;
    if (confirm("Do you wish to transfer money?")) {
        location.href = "/transfer"
    } else {
        alert("okay! Have a good day!")
    }
    document.getElementById("transfer").innerHTML = submission;
}

 function msg(){
        alert("Transfer was a success!");
}