export default class RegisterApi { 
  constructor(instance) { 
    this.API = instance 
  } 
 
  userRegister = async (data) => { 
    return this.API({ 
      method: 'POST', 
      url: '/register', 
      data, 
      headers: { 
        'Content-Type': 'application/json' 
      } 
    }) 
  } 
}