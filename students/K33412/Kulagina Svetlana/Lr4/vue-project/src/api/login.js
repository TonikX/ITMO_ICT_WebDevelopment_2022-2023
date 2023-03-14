export default class LoginApi { 
  constructor(instance) { 
    this.API = instance 
  } 
 
  userLogin = async (data) => { 
    return this.API({ 
      method: 'POST', 
      url: '/login', 
      data, 
      headers: { 
        'Content-Type': 'application/json' 
      } 
    }) 
  } 
}