import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        cart: {
            items: []
        },
    },
    getters: {
        getItems (state) {
            return state.cart.items
        },
        getItem: (state) => (id) => {
            return state.cart.items.find(item => item.id === id)
        },
        getTotal (state) {
            return state.cart.items.reduce((summ, item) => {
                return summ + (item.price * item.qty)
            }, 0)
        }
    },
    mutations: {
        SET_CART (state, cart) {
            state.cart = cart
        },
        ADD_TO_CART (state, item) {
            state.cart.items.push(item)
        },
        INCREMENT_ITEM_QTY (state, id) {
            state.cart.items.find(item => {
                if (item.id === id) item.qty++
            })
        }
    },
    actions: {
        getCartItems ({commit}) {
            commit('SET_CART', Vue.$storage.get('cart'))
        },
        addItemToCart ({state, commit, getters}, item) {
            if (getters.getItem(item.id)) {
                commit('INCREMENT_ITEM_QTY', item.id)
            } else {
                commit('ADD_TO_CART', item)
            }
            Vue.$storage.set('cart', state.cart)
        }
    }
})
