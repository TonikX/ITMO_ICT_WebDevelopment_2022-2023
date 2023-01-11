class WorkersApi {
    constructor(instance) {
      this.API = instance
    }
    
    getAll = async () => {
      return this.API({
        url: '/api/create_worker/'
      })
    }
    
    createWorker = async (data) => {
      return this.API({
        method: 'POST',
        url: '/api/create_worker/',
        data,
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }

    getCurrentWorker = async (id) => {
        return this.API({
            method: 'GET',
            url: '/api/get_worker/' + id,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    changeWorker = async (data) => {
        return this.API({
            method: 'PUT',
            url: '/api/update_worker/' + localStorage.needed_table_number,
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    deleteWorker = async () => {
        return this.API({
            method: 'DELETE',
            url: '/api/update_worker/' + localStorage.needed_table_number,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

   }
    
   export default WorkersApi
