class ScenariosAPI {
    constructor(instance) {
        this.API = instance
    }

    getAllScenarios = async (authToken) => {
        if(authToken) {
            return this.API({
                method: 'GET',
                url: 'scenarios/scenarios',
                headers: {
                    'Authorization': `token ${authToken}`,
                }
            })
        }
        return this.API({
            method: 'GET',
            url: 'scenarios/scenarios',
        })
    }

    getScenarioById = async (id) => {
        return this.API({
            method: 'GET',
            url: `scenarios/scenarios/${id}`,
        })
    }

    getFilteredScenarios = async (seacrhParams) => {
        const params = new URLSearchParams();
        for (const [key, value] of Object.entries(seacrhParams)) {
            for (const element of value) {
                params.append(key, element);
            }
        }

        return this.API({
            method: 'GET',
            url: 'scenarios/scenarios',
            params: params
        })
    }

    createScenario = async (data) => {
        return this.API({
            method: 'POST',
            url: 'scenarios/scenarios/create',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }

    likeScenario = async (id, authToken) => {
        return this.API({
            method: 'PATCH',
            url: `scenarios/scenarios/${id}/likes/update/`,
            headers: {
                'Authorization': `token ${authToken}`,
            },
        })
    }

    createScenarioReview = async (text, id, authToken) => {
        return this.API({
            method: 'POST',
            url: `scenarios/scenarios/${id}/reviews/create/`,
            data: {
                text: text
            },
            headers: {
                'Authorization': `token ${authToken}`,
            }
        })
    }
}

export default ScenariosAPI
