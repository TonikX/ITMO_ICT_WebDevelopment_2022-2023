class enrollmentsApi {
    constructor(instance){
        this.API = instance
    }

    getUserEnrollments = async (id) => {
        return this.API({
            url: `/api/enrollments/all?user_id=${id}`,
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            }
        })
    } 

    deleteUserEnrollment = async (id) => {
        return this.API(({
            url: `/api/enrollments/${id}/delete`,
            method: 'DELETE'
        }))
    }

    makeUserEnrollment = async (data) => {
        return this.API(({
            url: `/api/enrollments/new`,
            method: 'POST',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        }))
    }
}
export default enrollmentsApi