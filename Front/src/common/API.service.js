// Funcion for API communication

import {CSRFToken} from "./CSRF_token.js"

async function getJSON(response) {
  if (response.status === 204) return '';
  return response.json();
}

function APIService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      'content-type': 'application/json',
      'X-CSRFToken': CSRFToken
    }
  }; return fetch(endpoint, config)
  .then(getJSON)
  .catch(error => console.log(error))
}

export {APIService};
