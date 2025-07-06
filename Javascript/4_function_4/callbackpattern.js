let paymentSuccess = true;
let marks = 80;

function enroll(callback) {
    console.log("Enrolling...");
    setTimeout(() => {
        if(paymentSuccess) {
            callback();
            console.log("Payment successful");
        }
        else {
            console.log("Payment failed");
        }
    }, 2000);
}

function progress(callback) {
    console.log("Processing...");
    setTimeout(() => {
        if(marks>=80) {
            callback();
            console.log("Your certificate is generated successfully");
        }
        else {
            console.log("You are not eligible for the certificate");
        }
    }, 2000);
}

function getCertificate() {
    console.log("Getting certificate...");
}
enroll(function() {
    progress(getCertificate);
});


