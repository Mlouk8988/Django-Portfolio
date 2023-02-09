const username = document.getElementById('username')
const email = document.getElementById('email')
const subject = document.getElementById('subject')
const message = document.getElementById('message')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')


form.addEventListener('submit', (e) => {
  let messages = []

  if (username.value === '') {
    messages.push('Name is required')
  }

  if (subject.value === '') {
    messages.push('subject is required')
  }

  if (message.value.length <= 15) {
    messages.push('message must be more than 15 characters')
  }

 

  if (messages.length > 0) {
    e.preventDefault()
    errorElement.innerText = messages.join(', ')
  }
});

