/* Contact Us related */
const mailSentSuccessfully = () => {
    /*
    interacts with the user in case of successful "contact us" mail send
    */
    if (!document.getElementById("successNotice")) { /* Handle multi submissions - check if element doesn't exist already */
        let successNotice = document.createElement("p");
        successNotice.id = "successNotice";
        successNotice.innerHTML = "Message Sent !";
        let submitButtonContainer = document.getElementsByClassName("submit-button-container")[0];
        submitButtonContainer.appendChild(successNotice);
        successNotice.style.display = "inline";
        successNotice.style.paddingLeft = "10px";
    } else {
        document.getElementById("successNotice").innerHTML = "Sent another :) WE LOVE E-MAILS !";
    }
}


const handleContactUsSubmit = () => {
    /* send Contact Us form to backend and interacts with the client accordingly */
    const form = document.getElementById("contact-form");
    fetch("./send_message", { method: 'POST', body: new FormData(form)}).then(response => {
        mailSentSuccessfully()
      }).catch(error => {
            console.error('Error!', error.message);
            alert("Could not be sent. Please Try Again Later.");
        })
    form.reset();
}
