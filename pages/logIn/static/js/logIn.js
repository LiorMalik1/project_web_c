const myForm3 = document.querySelector('.my-form3')
const username_Input = document.querySelector('#user_name')
const password_Input = document.querySelector('#Password')
const msg3 = document.querySelector('.msg3')

const onSubmit = (e) => {
    e.preventDefault()

    //isEmpty
    if (username_Input.value === '' || password_Input.value === ''){
      console.log('fields empty')
        msg3.innerHTML ="Please fill out all fields";
    }

    //validPassword
    else if (password_Input.value.length<8){
      console.log('not valid password')
      msg3.innerHTML ="please enter a password with more than 7 characters";
    }
    else {

        myForm3.submit();
    }
}
myForm3.addEventListener('submit', onSubmit)
