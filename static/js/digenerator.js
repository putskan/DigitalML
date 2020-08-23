const digenerate = async () => {
    try {
        let digenerateQueryResponse = await fetch('./digenerate_backend_query');
        if (digenerateQueryResponse) {
            /* parse to dictionary */
            let digenerateResult = await digenerateQueryResponse.json(); /* convery json to object */
            let imagePath = digenerateResult['image_path'];
            let title = digenerateResult['name'];
            let description = digenerateResult['description'];
            assignDigenerateValues(imagePath, title, description);
            return ""
        }
        throw new Error('Request failed!');
    } catch (error) {
        console.log(error); 
  }
}

const assignDigenerateValues = (imagePath, title, description) => {
    /* assign the digenerate content to the webpage */
    let imgElement = document.getElementById("digenerated-product-img")
    let titleElement = document.getElementById("digenerated-product-title")
    let descriptionElement = document.getElementById("digenerated-product-description")

    imgElement.src = imagePath;
    titleElement.innerHTML = title;
    descriptionElement.innerHTML = description;
    return ""
}

/* main */
window.onload = function() {
    digeneratorButton = document.getElementById("digenerator-button");
    digeneratorButton.addEventListener("click", digenerate)
}

