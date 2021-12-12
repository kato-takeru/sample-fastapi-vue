import { createStore } from 'vuex'

export const store = createStore({
    state: {
        trends: [],
    },
    mutations: {
        setTrends(state, trends) {
            state.trends = trends;
        }
    }
})