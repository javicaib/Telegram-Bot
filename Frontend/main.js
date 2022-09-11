var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };
  
  fetch("http://127.0.0.1:8000/api/game/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));