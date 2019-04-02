import Vue from 'vue'
import './plugins/axios'
import store from './store'
import CategoriesTile from './components/CategoriesTile'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ru-RU'
import './assets/styles/app.scss'
import UIkit from 'uikit'
import '@/assets/styles/styles.scss'

window.UIkit = UIkit

Vue.use(ElementUI, {locale})

Vue.config.productionTip = false

new Vue({
    el: '#app',
    store,
    components: {
        CategoriesTile
    }
})
