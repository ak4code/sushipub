import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        cart: {
            items: [],
            delivery: 0,
        },
    },
    getters: {
        getItems (state) {
            return state.cart.items
        },
        getDelivery (state) {
            return state.cart.delivery
        },
        getItem: (state) => (id) => {
            return state.cart.items.find(item => item.product.id === id)
        },
        getTotal (state) {
            let items = state.cart.items.reduce((summ, item) => {
                return summ + (item.product.price * item.qty)
            }, 0)
            if (!items) {
                return 0
            } else {
                return items + state.cart.delivery
            }
        }
    },
    mutations: {
        SET_CART (state, cart) {
            state.cart = cart
        },
        ADD_TO_CART (state, item) {
            state.cart.items.push(item)
        },
        DELETE_ITEM_CART (state, index) {
            state.cart.items.splice(index, 1)
        },
        INCREMENT_ITEM_QTY (state, id) {
            state.cart.items.find(item => {
                if (item.product.id === id) item.qty++
            })
        },
        DECREMENT_ITEM_QTY (state, id) {
            state.cart.items.find(item => {
                if (item.product.id === id) item.qty--
            })
        },
        SET_ITEM_QTY (state, i) {
            state.cart.items.find(item => {
                if (item.product.id === i.product.id) item.qty = i.qty
            })
        },
        SET_DELIVERY (state, price) {
            state.cart.delivery = price
        },
        RESET_CART (state) {
            state.cart = {
                items: [],
                delivery: 0,
            }
        }
    },
    actions: {
        getCartItems ({state, commit}) {
            if (!Vue.$storage.get('cart')) {
                Vue.$storage.set('cart', state.cart)
            }
            commit('SET_CART', Vue.$storage.get('cart'))
        },
        addItemToCart ({state, commit, getters}, item) {
            if (getters.getItem(item.product.id)) {
                commit('INCREMENT_ITEM_QTY', item.product.id)
            } else {
                commit('ADD_TO_CART', item)
            }
            Vue.$storage.set('cart', state.cart)
        },
        changeItemCart ({state, commit}, item) {
            commit('SET_ITEM_QTY', item)
            Vue.$storage.set('cart', state.cart)
        },
        deleteItemCart ({state, commit}, index) {
            commit('DELETE_ITEM_CART', index)
            Vue.$storage.set('cart', state.cart)
        },
        resetCart ({state, commit}) {
            commit('RESET_CART')
            Vue.$storage.set('cart', state.cart)
        }
    }
})
