import Vue from 'vue'
import Pusher from 'pusher-js'

Pusher.logToConsole = process.env.NODE_ENV === 'production' ? false : true

const _pusher = new Pusher(process.env.VUE_APP_PUSHER_KEY, {
    cluster: 'eu',
    forceTLS: true
})

const PusherPlugin = {

    install (Vue, options) {
        Object.defineProperties(Vue.prototype, {
            $pusher: {
                get () {
                    return _pusher;
                }
            },
        });
    }
};

Vue.use(PusherPlugin)

export default PusherPlugin