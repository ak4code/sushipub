import Vue from 'vue'
import Vue2Storage from 'vue2-storage'

Vue.use(Vue2Storage, {
    prefix: 'app_',
    driver: 'local',
    ttl: 60 * 60 * 24 * 1000
})

if (!Vue.$storage.get('cart')) {
    Vue.$storage.set('cart', {items: []})
}