import Vue from 'vue'
import './plugins/axios'
import './plugins/pusher'
import './plugins/vue2storage'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ru-RU'
import './assets/styles/app.scss'
import UIkit from 'uikit'
import '@/assets/styles/styles.scss'
import store from './store'
import ProductShort from './components/shop/ProductShort'
import CategoryDetail from './components/shop/CategoryDetail'
import CartButton from './components/shop/CartButton'
import CartPage from './components/shop/CartPage'


window.UIkit = UIkit

Vue.use(ElementUI, {locale})

Vue.config.productionTip = false

new Vue({
    el: '#app',
    store,
    components: {
        ProductShort,
        CategoryDetail,
        CartButton,
        CartPage
    }
})
