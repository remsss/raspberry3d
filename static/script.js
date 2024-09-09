function myFunction(button) {
    console.log('hello world send by', button)
  }

function modifyImg() {
    fetch('rimg').then(location.reload())
}

function CPUTemp() {
    fetch('info')
        .then((response) => {
            console.log(response);
            return response.json();
        })
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}


function shutdownSite() {
    fetch('shutdownSite').then(location.reload())
}

function StopPrint() {
fetch('stopprint')
}

function pprint() {
    fetch('pprint')
}

